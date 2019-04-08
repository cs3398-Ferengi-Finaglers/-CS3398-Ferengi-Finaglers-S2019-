from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=2000, default = "Add more info to your profile!", blank = False)
    #GP = models.TextField(max_length = 5000, default = "Add the games you are playing here!", blank = False)

    def __str__(self):
        return self.user

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user = instance)

# Create your models here.
