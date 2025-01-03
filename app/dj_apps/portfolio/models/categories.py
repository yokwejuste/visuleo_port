from django.db import models
from app.dj_apps.users.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Categories(BaseModel):
    """
    Model that represents a category.
    """

    name = models.CharField(
        _("name"),
        max_length=255,
        help_text=_("Name of the category."),
    )
    slug = models.SlugField(
        _("slug"),
        max_length=255,
        unique=True,
        help_text=_("Slug of the category."),
    )
    description = models.TextField(
        _("description"),
        help_text=_("Description of the category."),
    )

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ("name",)
        db_table = "categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
