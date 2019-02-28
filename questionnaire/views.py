from django.shortcuts import render
from django.http import HttpResponse

from .models import Questions, Answers

# Create your views here.
def index(request):
	#return HttpResponse("Welcome to the questionnaire.")
	questions = Questions.objects.all()[:1]
	answers = Answers.objects.all()
	
	context = {
		'questions': questions,
		'answers': answers,
	}
	
	return render(request, 'questionnaire/index.html', context)