from django.urls import path
from registration import views as register_views

urlpatterns = [
	path('register/', register_views.register, name='Register'),
]