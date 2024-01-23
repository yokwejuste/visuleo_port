from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registration.
    """

    class Meta:
        model = User
        fields = (
            "name",
            "email",
            "password",
            "phone_number",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "phone_number": {"required": True},
        }

    def create(self, validated_data):
        """
        Create a new user.
        """
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for login.
    """

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user.
    """

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = (
            "id",
            "is_superuser",
            "last_login",
        )


class UserMainSerializer(serializers.ModelSerializer):
    """
    Serializer for user.
    """

    class Meta:
        model = User
        fields = "__all__"


class UserResponseSerializer(serializers.Serializer):
    """
    Serializer for user.
    """

    token = serializers.CharField()
    token_type = serializers.CharField()
    expires_in = serializers.IntegerField()
    refresh_token = serializers.CharField()
    scope = serializers.CharField()
    user = UserSerializer(many=False)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = (
            "id",
            "is_email_verified",
            "is_phone_number_verified",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
        )
