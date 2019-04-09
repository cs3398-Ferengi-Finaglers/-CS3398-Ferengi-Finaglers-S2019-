from django import forms
from django.forms.widgets import RadioSelect
from .models import *

class MatchmakingForm(forms.ModelForm):
	class Meta:
		model = Matchmaking
		fields = ('k',) #We only want this one exposed