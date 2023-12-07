from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender = User)
def post_save_funct(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        updated_user_profile = UserProfile.objects.get(user=instance)
        updated_user_profile.save()

@receiver(pre_save, sender = User)
def pre_save_funct(sender, instance, **kwargs):
    print(instance.username, "The user is created")
       