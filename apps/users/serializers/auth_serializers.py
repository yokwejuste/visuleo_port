from apps.users.models import VisuleoUser as User
from rest_framework import serializers



class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registration.
    """

    class Meta:
        model = User
        exclude = (
            "is_email_verified",
            "is_phone_number_verified",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
            'is_deleted',
            'id'
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
