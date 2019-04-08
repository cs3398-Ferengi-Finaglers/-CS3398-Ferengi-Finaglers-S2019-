from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from questionnaire.views import indexRedirectView

urlpatterns = [
	path('', views.index, name='matchmakingindex'),
]