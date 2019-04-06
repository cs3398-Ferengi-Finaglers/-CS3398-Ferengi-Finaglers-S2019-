from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_pk>', views.profile, name='profile'),
    path('profileEdit/<int:user_pk>', views.EditProfile, name='EditProfile')
]