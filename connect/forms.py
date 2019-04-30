from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render
      
USERS = User.objects.all()

#class ReceiveForm(forms.Form):
#	class Meta:
#		model = FriendRequests.objects.filter(user=2, friendship=False)
	#	fields = ['request']

#class ReceiveForm(forms.Form):

#	def __init__(self,*args,**kwargs):
#		choices = kwargs.pop('choices')

#		super(ReceiveForm,self).__init__(*args,**kwargs)
		
#		self.fields['new_friendship'].choices = choices
		
#	new_friendship = forms.CharField(label='', widget=forms.CheckboxSelectMultiple, choices=[])
