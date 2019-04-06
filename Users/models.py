from django.db import models
from django.contrib.auth.models import User
from django.db.mdoels.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Models):
    user = models.OneToOneFiled(User,on_delete=models.CASCADE, related_name='profile')
    bio = model.TextField(max_length=2000, default = "Add more info to your profile!", blank = False)

    def __str__(self):
        return self.user

    @reciever(psot_save, sender=User)
    def update_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user = instance)

# Create your models here.
