from django.db import models
from django.utils.translation import gettext_lazy as _

from app.dj_apps.users.models import BaseModel


class Volunteering(BaseModel):
    """
    Models  for volunteering experience
    """

    title = models.CharField(
        _("Title"),
        max_length=255,
        help_text=_("Title of the volunteering experience."),
    )
    organization = models.CharField(
        _("Organization"),
        max_length=255,
        help_text=_("Organization of the volunteering experience."),
    )
    start_date = models.DateField(
        _("Start Date"),
        null=True,
        blank=True,
        help_text=_("Start date of the volunteering experience."),
    )
    end_date = models.DateField(
        _("End Date"),
        null=True,
        blank=True,
        help_text=_("End date of the volunteering experience."),
    )
    image = models.ImageField(
        _("Image"),
        upload_to="volunteering/",
        blank=True,
        null=True,
        help_text=_("Image for the volunteering experience."),
    )
