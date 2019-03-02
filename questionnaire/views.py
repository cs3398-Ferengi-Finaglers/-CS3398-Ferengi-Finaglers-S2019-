from django.shortcuts import render
from django.http import HttpResponse

from .models import Questions, Answers

# Create your views here.
def index(request):
	#to only display the first question:
	#questions = Questions.objects.all()[:1]
	#to display all questions:
	questions = Questions.objects.all()

	context = {
		'questions': questions,
	}
	
	return render(request, 'questionnaire/index.html', context)