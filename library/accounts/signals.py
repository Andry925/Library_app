from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_funct(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            updated_user_profile = UserProfile.objects.get(user=instance)
            updated_user_profile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def pre_save_funct(instance,**kwargs):
    print(instance.username, "The user is created")
