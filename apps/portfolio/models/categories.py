from django.db import models
from apps.users.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse



class Categories(BaseModel):
    """
    Model that represents a category.
    """
    name = models.CharField(
        _('name'),
        max_length=255,
        help_text=_('Name of the category.'),
    )
    description = models.TextField(
        _('description'),
        help_text=_('Description of the category.'),
    )
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
    
    def __str__(self) -> str:
        return self.name