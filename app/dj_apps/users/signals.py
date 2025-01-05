from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from app.dj_apps.users.middlewares.user_tracing import get_current_user
from app.dj_apps.users.models import BaseModel
from app.dj_apps.users.models import VisuleoUser, UserTag


@receiver(post_save, sender=VisuleoUser)
def add_user_tag(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        user_tag, created = UserTag.objects.get_or_create(name="superuser")
        instance.tags.add(user_tag)
    elif created:
        user_tag, created = UserTag.objects.get_or_create(name="user")
        instance.tags.add(user_tag)


@receiver(post_save)
def log_activity(sender, instance, created, **kwargs):
    if issubclass(sender, BaseModel):
        current_user = get_current_user()
        user = current_user if current_user and current_user.is_authenticated else None
        action = "created" if created else "updated"
        print(f"User {user} {action} {instance}.")


@receiver(post_delete)
def log_deletion(sender, instance, **kwargs):
    if issubclass(sender, BaseModel):
        current_user = get_current_user()
        user = current_user if current_user and current_user.is_authenticated else None
        print(f"User {user} deleted {instance}.")
