from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from questionnaire.views import indexRedirectView

urlpatterns = [
	path('<int:question_pk>', views.index, name='questionnaire'),
	path('', indexRedirectView.as_view(), name='questionnaireindex'),
	path('complete', views.complete, name='questionnairecomplete'),
]