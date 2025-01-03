from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from app.dj_apps.users.models import BaseModel


class Talks(BaseModel):
    """
    Model that contains Talks.
    """

    date = models.DateField(
        _("Date"),
        help_text=_("Date of the talk."),
    )
    type = models.ForeignKey(
        "portfolio.TalksType",
        verbose_name=_(""),
        on_delete=models.CASCADE,
    )
    location = models.CharField(
        _("Location"),
        max_length=255,
        help_text=_("Location of the talk."),
    )
    languages = models.ManyToManyField(
        "portfolio.Languages",
        verbose_name=_("Languages"),
        related_name="talks",
        help_text=_("Languages used in the talk."),
    )
    title = models.CharField(
        _("Title"),
        max_length=255,
        help_text=_("Title of the talk."),
    )
    link = models.URLField(
        _("Link"),
        blank=True,
        null=True,
        max_length=255,
        help_text=_("Link to the talk."),
    )
    slug = models.SlugField(
        _("Slug"),
        max_length=255,
        unique=True,
        help_text=_("Slug for the talk."),
    )

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Talks, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Talk")
        verbose_name_plural = _("Talks")
        db_table = "talks"


class TalksType(BaseModel):
    """
    Model that contains the type of the talk.
    """

    name = models.CharField(
        _("Name"),
        max_length=255,
        help_text=_("Name of the type of the talk."),
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Talk Type")
        verbose_name_plural = _("Talk Types")
        db_table = "talks_type"


class Languages(BaseModel):
    """
    Model that contains the languages.
    """

    name = models.CharField(
        _("Name"),
        max_length=255,
        help_text=_("Name of the language."),
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")
        db_table = "languages"
