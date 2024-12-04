from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import BaseModel
from django.utils.text import slugify


class Skills(BaseModel):
    """
    Model that represents a skill.
    """

    name = models.CharField(
        _("name"),
        max_length=255,
        help_text=_("Name of the skill."),
    )
    description = models.TextField(
        _("description"),
        help_text=_("Description of the skill."),
    )
    is_featured = models.BooleanField(
        _("is featured"),
        default=False,
        help_text=_("Boolean field to mark if this skill is featured."),
    )

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")
        db_table = "skills"

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Skills, self).save(*args, **kwargs)
