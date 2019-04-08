from django.contrib import admin

# Register your models here.
from .models import Friends

admin.site.register(Friends)


# Friendslist model
# class FriendsList(admin.ModelAdmin):
#   list_display = ("friend", "friend")
