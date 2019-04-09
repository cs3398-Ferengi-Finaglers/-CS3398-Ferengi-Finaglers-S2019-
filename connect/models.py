from django.db import models
from django.contrib.auth.models import User
from .forms import SendForm

# Create your models here.

class FriendRequests(models.Model):
	request = models.ManyToManyField(User)
	user = models.ForeignKey(User, related_name= "owner", null=True, on_delete=models.CASCADE)
	friendship = models.BooleanField(default=False)