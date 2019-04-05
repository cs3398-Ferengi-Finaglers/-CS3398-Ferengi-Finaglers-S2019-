from django.urls import path
from . import views as register_views

urlpatterns = [
	path('', register_views.register, name='Register')
]