from django import forms
from django.forms.widgets import RadioSelect
from .models import *
from . import widgets

class MatchmakingForm(forms.ModelForm):
	class Meta:
		model = Matchmaking
		fields = ('k',) #We only want this one exposed
		
class UserRatingForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserRatingForm, self).__init__(*args, **kwargs)

		self.fields['aggressionRating'].widget = widgets.RatingInput(attrs={'max':'5', 'class': 'slider',})
		self.fields['skillRating'].widget = widgets.RatingInput(attrs={'max':'5', 'class': 'slider',})
		self.fields['teamworkRating'].widget = widgets.RatingInput(attrs={'max':'5', 'class': 'slider',})
		self.fields['communicationRating'].widget = widgets.RatingInput(attrs={'max':'5', 'class': 'slider',})
		
	class Meta:
		model = UserRating
		fields = ('aggressionRating', 'skillRating', 'teamworkRating', 'communicationRating') #We only want this one exposed