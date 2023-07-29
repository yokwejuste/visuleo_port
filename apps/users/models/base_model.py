from django.db import models
from django.utils.translation import gettext_lazy as _
from utils import generate_uuid


class BaseModelDeletionManager(models.Manager):
    """
    Custom model manager that returns all objects, including those that are
    deleted.
    """
    def get_queryset(self):
        return super().get_queryset()
    
    def all_with_deleted(self):
        return super().get_queryset().filter(is_deleted=True)



class BaseMdeoelManager(models.Manager):
    """
    Custom model manager that returns only objects that are not deleted.
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
    def all_with_deleted(self):
        return super().get_queryset()


class BaseModel(models.Model):
    """
    Abstract model that provides self-updating ``created`` and ``modified``
    fields.
    """
    id = models.UUIDField(
        _('id'),
        primary_key=True,
        default=generate_uuid,
        editable=False,
        help_text=_('Unique identifier for this object.'),
    )
    created = models.DateTimeField(
        _('created'),
        auto_now_add=True,
        help_text=_('Date and time when this object was created.'),
    )
    modified = models.DateTimeField(
        _('modified'),
        auto_now=True,
        help_text=_('Date and time when this object was last modified.'),
    )
    is_deleted = models.BooleanField(
        _('is deleted'),
        default=False,
        help_text=_('Boolean field to mark if this object is deleted.'),
    )
    
    objects = BaseMdeoelManager()

    deleted_obkects = BaseModelDeletionManager()


    class Meta:
        abstract = True
        ordering = ('-created', '-modified',)