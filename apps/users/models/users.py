from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from apps.users.models import BaseModel


class VisuleoUser(BaseModel, AbstractUser):
    """
    Custom user model for Visuleo.
    """
    name = models.CharField(
        _('name'),
        max_length=255,
        blank=True,
        help_text=_('User\'s full name.'),
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        help_text=_('User\'s email address.'),
    )
    phone_number = models.CharField(
        _('phone number'),
        max_length=20,
        blank=True,
        help_text=_('User\'s phone number.'),
    )
    is_email_verified = models.BooleanField(
        _('is email verified'),
        default=False,
        help_text=_('Boolean field to mark if this user\'s email is verified.'),
    )
    is_phone_number_verified = models.BooleanField(
        _('is phone number verified'),
        default=False,
        help_text=_('Boolean field to mark if this user\'s phone number is verified.'),
    )
    is_active = models.BooleanField(
        _('is active'),
        default=True,
        help_text=_('Boolean field to mark if this user is active.'),
    )
    is_superuser = models.BooleanField(
        _('is superuser'),
        default=False,
        help_text=_('Boolean field to mark if this user is superuser.'),
    )
    last_login = models.DateTimeField(
        _('last login'),
        default=timezone.now,
        help_text=_('Date and time when this user last logged in.'),
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now,
        help_text=_('Date and time when this user joined.'),
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-created', '-modified',)
    
    def __str__(self) -> str:
        return self.email
    