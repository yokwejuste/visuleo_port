import secrets
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from apps.users.serializers import (
    RegistrationSerializer,
    LoginSerializer,
    UserResponseSerializer,
)
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from oauth2_provider.models import Application, AccessToken, RefreshToken
from oauth2_provider.views import TokenView
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from django.core.management import call_command
from drf_yasg.utils import swagger_auto_schema
from django.utils.timezone import now

from utils.main import load_document


User = get_user_model()

email_content_type = "text/html"


class RegistrationView(generics.CreateAPIView):
    authentication_classes = [
        BasicAuthentication,
    ]
    serializer_class = RegistrationSerializer
    permission_classes = [
        AllowAny,
    ]

    @swagger_auto_schema(
        operation_id="Register a user",
        operation_summary="Register a new user",
        request_body=RegistrationSerializer,
        tags=["Authentication and Management"],
        responses={
            201: "You will be rerouted to the confirmation page",
            300: "Multiple choices",
            400: "Bad request",
            500: "Internal server error",
        },
    )
    def post(self, request):
        if not request.data:
            return Response(
                {"error": "Please provide the required fields"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        phone_number = serializer.validated_data.get("phone_number")
        username = serializer.validated_data.get("username")
        try:
            if (
                email
                and User.objects.exclude(email__isnull=True)
                .exclude(email__exact="")
                .filter(email=email.lower())
                .exists()
            ):
                return Response(
                    {"error": "User with this email already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if (
                phone_number
                and User.objects.exclude(phone_number__isnull=True)
                .exclude(phone_number__exact="")
                .filter(phone_number=phone_number)
                .exists()
            ):
                return Response(
                    {"error": "User with this phone number already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if (
                username
                and User.objects.exclude(username__isnull=True)
                .exclude(username__exact="")
                .filter(username=username)
                .exists()
            ):
                return Response(
                    {"error": "User with this username already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except IntegrityError:
            return Response(
                {"error": "Integrity error"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = serializer.save()
        user.save()
        return Response(
            {"success": "User registered successfully. Go ahead and login."},
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView, TokenView):
    serializer_class = LoginSerializer
    authentication_classes = [
        OAuth2Authentication,
    ]
    permission_classes = [
        AllowAny,
    ]

    def authenticate(self, request, email_or_phone=None, password=None):
        try:
            user = User.objects.get(
                Q(email=email_or_phone) | Q(phone_number=email_or_phone)
            )
            if user.check_password(password):
                if not user.is_active:
                    raise ValueError("User account is not active")
                if not user.phone_number_verified and email_or_phone.startswith("+"):
                    raise ValueError("Phone number not verified")
                return user
        except User.DoesNotExist:
            return None

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    @swagger_auto_schema(
        operation_id="Login",
        operation_summary="Login a user",
        operation_description=load_document("auth/login_docs.html"),
        request_body=LoginSerializer,
        tags=["Authentication and Management"],
        responses={
            200: UserResponseSerializer,
            300: "Multiple choices",
            400: "Bad request",
            500: "Internal server error",
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        expiration_time = now() + timedelta(hours=3600)
        success_message = "User logged in successfully"

        try:
            user = self.authenticate(
                request,
                email_or_phone=data.get("email_or_phone"),
                password=data.get("password"),
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        if user and not user.is_active:
            return Response(
                {"error": "User account is not active"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not user:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            try:
                application = Application.objects.get(name="Default")
                access_token = AccessToken.objects.create(
                    user=user,
                    application=application,
                    expires=expiration_time,
                    token=secrets.token_hex(16),
                )
                refresh_token = RefreshToken.objects.create(
                    user=user,
                    application=application,
                    token=secrets.token_hex(16),
                )
                refresh_token.access_token = access_token
                refresh_token.save()
                user.save(set_active=True)
            except ObjectDoesNotExist:
                call_command("activate_app")
                return Response(
                    {"error": "Please try again the server is restarting"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        response_data = {
            "success_message": success_message,
            "access_token": access_token.token,
            "refresh_token": refresh_token.token,
            "token_type": "Bearer",
            "expires_in": f"{(expiration_time - now()).seconds // 3600} hours",
            "user": UserResponseSerializer(user).data,
        }
        return Response(response_data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    authentication_classes = [
        OAuth2Authentication,
    ]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="Logout Current User",
        tags=["Authentication and Management"],
        responses={
            200: "User logged out successfully",
            500: "Server Error",
        },
    )
    def post(self, request):
        user = request.user
        app = Application.objects.get(name="Default")
        tokens = AccessToken.objects.filter(user=user, application=app)
        for token in tokens:
            token.delete()
        user.save(set_active=True)
        return Response(
            {"message": "User logged out successfully"},
            status=status.HTTP_200_OK,
        )
