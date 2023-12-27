from django.db.models.signals import post_save,pre_save
from .models import CustomUser,Profile
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(pre_save, sender=Profile)
def update_user_is_verified(sender, instance, **kwargs):
    if instance.user.is_verified:
        return 
    instance.user.is_verified = True
    instance.user.save()