from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Whenever a User is saved, if it's a new record (created=True), 
    we automatically create a Profile linked to that user.
    """
    if created:
        Profile.objects.create(user=instance)