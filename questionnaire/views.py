from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic.base import RedirectView
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request, question_pk):
	question = get_object_or_404(Questions, pk=question_pk)
	
	if request.method == 'POST':
		form = ResponseInstancesForm(question, request.POST)  #<-- Note the extra arg
		if form.is_valid():
			responseInstance = form.save(commit=False)
			if request.user.is_authenticated:
				#responseInstance.user = None
				responseInstance.user = request.user
			else:
				responseInstance.user = None
			responseInstance.question = question
			responseInstance.save()
			
			question_pk += 1
			try: 
				Questions.objects.get(pk=question_pk)
				return redirect('questionnaire', question_pk=question_pk)
			except Questions.DoesNotExist:
				return redirect('questionnairecomplete')
	else:
		form = ResponseInstancesForm(question)

	context = {
		'form': form,
		'question': question,
	}
	
	return render(request, 'questionnaire/index.html', context)
	
class indexRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'questionnaire'

    def get_redirect_url(self, *args, **kwargs):
        if 'question_pk' not in kwargs.keys():
            kwargs = {'question_pk': 1}
        question = get_object_or_404(Questions, pk=kwargs['question_pk'])
        return super().get_redirect_url(*args, **kwargs)
		
def complete(request):
	#return HttpResponse("Hello world! You are now inside one of django's views.")
	return render(request, 'questionnaire/complete.html')