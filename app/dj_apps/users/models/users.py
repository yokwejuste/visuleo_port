from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from app.dj_apps.users.models import BaseModel


class VisuleoUserManager(BaseUserManager):
    """
    Custom user model manager for Visuleo.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a Visuleo user with the given email and password.
        """
        if not email:
            raise ValueError(_("The email must be set."))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a Visuleo superuser with the given email and password.
        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self.create_user(email, password, **extra_fields)


class VisuleoUser(BaseModel, AbstractBaseUser):
    """
    Custom user model for Visuleo.
    """

    username = models.CharField(
        _("username"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("User's username."),
    )
    name = models.CharField(
        _("name"),
        max_length=255,
        blank=True,
        help_text=_("User's full name."),
    )
    email = models.EmailField(
        _("email address"),
        unique=True,
        help_text=_("User's email address."),
    )
    phone_number = models.CharField(
        _("phone number"),
        max_length=20,
        blank=True,
        help_text=_("User's phone number."),
    )
    email_verified = models.BooleanField(
        _("is email verified"),
        default=False,
        help_text=_("Boolean field to mark if this user's email is verified."),
    )
    phone_number_verified = models.BooleanField(
        _("is phone number verified"),
        default=False,
        help_text=_("Boolean field to mark if this user's phone number is verified."),
    )
    is_active = models.BooleanField(
        _("is active"),
        default=True,
        help_text=_("Boolean field to mark if this user is active."),
    )
    is_superuser = models.BooleanField(
        _("is superuser"),
        default=False,
        help_text=_("Boolean field to mark if this user is superuser."),
    )
    last_login = models.DateTimeField(
        _("last login"),
        default=timezone.now,
        help_text=_("Date and time when this user last logged in."),
    )
    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
        help_text=_("Date and time when this user joined."),
    )
    is_staff = models.BooleanField(
        _("is staff"),
        default=False,
        help_text=_("Boolean field to mark if this user is staff."),
    )
    user_tag = models.ManyToManyField(
        "UserTag",
        verbose_name=_("user tag"),
        related_name="users",
        help_text=_("User tag for the user."),
    )

    objects = VisuleoUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = (
            "-created",
            "-updated",
        )
        db_table = "users"

    def __str__(self) -> str:
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class UserTag(BaseModel):
    """
    Model that represents a user type.
    """

    name = models.CharField(
        _("name"),
        max_length=255,
        help_text=_("Name of the user type."),
    )
    slug = models.SlugField(
        _("slug"),
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        help_text=_("Slug of the user type."),
    )

    class Meta:
        verbose_name = _("user type")
        verbose_name_plural = _("user types")
        ordering = ("name",)
        db_table = "user_tags"

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.lower())
        return super().save(*args, **kwargs)
