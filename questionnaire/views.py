from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic.base import RedirectView
from django.http import HttpResponse
from .models import *
from .forms import *
from Matchmaking.models import *

# Create your views here.
def index(request, question_pk):
	question = get_object_or_404(Questions, pk=question_pk)
	
	if request.method == 'POST':
		ResponseInstances.objects.filter(user=request.user).filter(question=question).delete() #delete past responses the user made to this question
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

	MatchmakingAttribute.objects.filter(user=request.user).delete() #delete past saved attributes the user has as they re-answered the questionnaire

	usersResponses = ResponseInstances.objects.filter(user=request.user)
	# For all question responses normalize the answer choosen to be out of 0 - 1
	# and store them in the normalizedValue list
	normalizedValue = []
	index = 0
	for response in usersResponses:
		print ("user's response " + str(index) + " = " + str(response.answer.KNNvalue))
		numOfAnswers = Answers.objects.filter(belongsTo=response.question)
		#find the highest KNNvalue given for a question's answer
		highestKNNValue = numOfAnswers[0].KNNvalue
		for i in numOfAnswers:
			if i.KNNvalue > highestKNNValue:
				highestKNNValue = i.KNNvalue
			
		print ("highestKNNValue = " + str(highestKNNValue))
		normalizedValue.append(response.answer.KNNvalue / highestKNNValue)
		print("normalizedValue = " + str(normalizedValue[index]) + "\n")
		index += 1
	#Take the average value for all responses pertaining to a certain attribute
	# and store them in the attributeValue list
	allAttributes = Attribute.objects.all()
	attributeValue = [0] * allAttributes.count()
	
	for i in range(allAttributes.count()):
		responsesWithAttribute = 0
		responseIndex = 0
		for response in usersResponses:
			
			if response.question.attribute == allAttributes[i]:
				print(str(allAttributes[i]) + " " + str(normalizedValue[responseIndex]))
				attributeValue[i] += normalizedValue[responseIndex]
				responsesWithAttribute += 1
			responseIndex += 1
		if responsesWithAttribute > 0: # make sure we are not dividing by zero
			attributeValue[i] = attributeValue[i] / responsesWithAttribute
		
		print("attribute " + str(i) + " value = " + str(attributeValue[i]))

	#Save the attributes to the user's matchmaking profile
	for i in range(allAttributes.count()):
		MatchmakingAttribute.objects.create(user = request.user,
											attribute = allAttributes[i],
											KNNvalue = attributeValue[i])
	
	return render(request, 'questionnaire/complete.html')