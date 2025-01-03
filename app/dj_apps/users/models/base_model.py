from django.db import models
from django.utils.translation import gettext_lazy as _

from app.dj_apps.users.middlewares.user_tracing import get_current_user


class BaseModelDeletionManager(models.Manager):
    """
    Custom model manager that returns all objects, including those that are
    deleted.
    """

    def get_queryset(self):
        return super().get_queryset()

    def all_with_deleted(self):
        return super().get_queryset().filter(is_deleted=True)


class BaseModelManager(models.Manager):
    """
    Custom model manager that returns only objects that are not deleted.
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def all_with_deleted(self):
        return super().get_queryset()


class BaseModel(models.Model):
    """
    Abstract model that provides self-updating ``created`` and ``updated``
    fields.
    """

    id = models.AutoField(
        _("id"),
        primary_key=True,
        editable=False,
        help_text=_("Unique identifier for this object."),
    )
    created = models.DateTimeField(
        _("created"),
        auto_now_add=True,
        help_text=_("Date and time when this object was created."),
    )
    updated = models.DateTimeField(
        _("updated"),
        auto_now=True,
        help_text=_("Date and time when this object was last updated."),
    )
    is_deleted = models.BooleanField(
        _("is deleted"),
        default=False,
        help_text=_("Boolean field to mark if this object is deleted."),
    )

    created_by = models.ForeignKey(
        "users.VisuleoUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_created_by",
        help_text=_("User who created this object."),
    )

    updated_by = models.ForeignKey(
        "users.VisuleoUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_updated_by",
        help_text=_("User who last updated this object."),
    )

    objects = BaseModelManager()

    deleted_objects = BaseModelDeletionManager()

    class Meta:
        abstract = True
        ordering = (
            "-created",
            "-updated",
        )

    def save(self, *args, **kwargs):
        current_user = get_current_user()
        if not self.pk and not self.created_by:
            self.created_by = (
                current_user if current_user and current_user.is_authenticated else None
            )
        self.updated_by = (
            current_user if current_user and current_user.is_authenticated else None
        )
        super().save(*args, **kwargs)
