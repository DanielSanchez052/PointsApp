from cProfile import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile
from apps.users.custom_auth.models import Auth


@receiver(post_save, sender=Profile)
def update_auth(sender, instance,created,**kwargs):
    if created:
        auth_user = Auth.objects.get(pk=instance.auth.id)
        auth_user.status = 2
        auth_user.save()