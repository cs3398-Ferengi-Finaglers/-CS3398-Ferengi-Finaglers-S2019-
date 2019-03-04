from django import forms
from django.forms.widgets import RadioSelect
from .models import *

class ResponseInstancesForm(forms.ModelForm):
	def __init__(self,question,*args,**kwargs):
		super(ResponseInstancesForm, self).__init__(*args,**kwargs) # populates the post
		#self.fields['answer'].queryset = Answers.objects.filter(belongsTo=question)
		#choice_list = question.getAnswers
		self.fields["answer"] = forms.ModelChoiceField(queryset=Answers.objects.filter(belongsTo=question),
                                                   widget=RadioSelect)
		self.fields['answer'].required=True
	class Meta:
		model = ResponseInstances
		fields = ('answer',) #We only want this one exposed