from django.db.models.signals import post_save
from django.dispatch import receiver
from app.dj_apps.users.models import VisuleoUser, UserTag
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from app.dj_apps.users.middlewares.user_tracing import get_current_user
from app.dj_apps.users.models import BaseModel


@receiver(post_save, sender=VisuleoUser)
def add_user_tag(sender, instance, created, **kwargs):
    if created:
        user_tag = UserTag.objects.create(user=instance, tag="user")
        user_tag.save()
    else:
        pass


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
