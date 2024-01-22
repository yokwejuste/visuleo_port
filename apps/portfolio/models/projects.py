from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from apps.users.models import BaseModel


class Projects(BaseModel):
    """
    Model that represents a project.
    """

    name = models.CharField(
        _("name"),
        max_length=255,
        help_text=_("Name of the project."),
    )
    slug = models.SlugField(
        _("slug"),
        max_length=255,
        unique=True,
        help_text=_("Slug for the project."),
    )
    description = models.TextField(
        _("description"),
        help_text=_("Description of the project."),
    )
    display_image = models.ImageField(
        _("image"),
        upload_to="projects/",
        help_text=_("Image for the project."),
    )
    url = models.URLField(
        _("url"),
        max_length=255,
        help_text=_("URL for the project."),
    )
    is_featured = models.BooleanField(
        _("is featured"),
        default=False,
        help_text=_("Boolean field to mark if this project is featured."),
    )
    categories = models.ManyToManyField(
        "Categories",
        verbose_name=_("categories"),
        related_name="projects",
        help_text=_("Categories for the project."),
    )

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("portfolio:project-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Projects, self).save(*args, **kwargs)


class ProjectImages(BaseModel):
    """
    Model that represents a project image.
    """

    project = models.ForeignKey(
        "Projects",
        verbose_name=_("project"),
        related_name="images",
        on_delete=models.CASCADE,
        help_text=_("Project for the image."),
    )
    image = models.ImageField(
        _("image"),
        upload_to="projects/",
        help_text=_("Image for the project."),
    )
    project_image_id = models.IntegerField(
        _("project image id"),
        help_text=_("Project image id."),
    )

    class Meta:
        verbose_name = _("project image")
        verbose_name_plural = _("project images")

    def save(self, *args, **kwargs):
        self.project_image_id = self.project.images.count() + 1
        super(ProjectImages, self).save(*args, **kwargs)

    def __str__(self):
        return self.project.name
