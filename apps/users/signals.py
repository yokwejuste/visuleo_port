from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import VisuleoUser, UserTag


@receiver(post_save, sender=VisuleoUser)
def add_user_tag(sender, instance, created, **kwargs):
    if created:
        user_tag = UserTag.objects.create(user=instance, tag='user')
        user_tag.save()
    else:
        pass
