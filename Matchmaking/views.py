from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic.base import RedirectView
from .models import *
from django.contrib.auth.models import User
from .forms import *
from .knn import *

# Create your views here.
def index(request):
	
	if request.method == 'POST':
		form = MatchmakingForm(request.POST)
		if form.is_valid():
			Matchmaking.objects.filter(user=request.user).delete() #delete past matchmakings/refresh response
			matchmakingInstance = form.save(commit=False)
			if request.user.is_authenticated:
				matchmakingInstance.user = request.user
			else:
				matchmakingInstance.user = None
			matchmakingInstance.save()
			
			#run knn algorithm
			
			# load all users and their attributes (except the current user) as a 2d list to be used as a dataset in knn
			dataset = [[0] * Attribute.objects.all().count() for i in range(User.objects.all().count())]
			loadDataset(dataset, request.user)
			print(dataset)
			
			# get the user's attributes to pass in to the knn getNeighbors function
			allAttributes = Attribute.objects.all()
			userInstance = [0] * allAttributes.count()
			attributeIndex = 0
			for attribute in allAttributes:
				try:
					userAttributeInstance = MatchmakingAttribute.objects.get(user=request.user, attribute=attribute)
				except MatchmakingAttribute.DoesNotExist:
					print('user ' + str(request.user) + ' does not have a value assigned for one of their attributes: '
					+ str(attribute))
					dataset[i.id - 1][attributeIndex] = 0
					break
				
				userInstance[attributeIndex] = userAttributeInstance.KNNvalue
				attributeIndex += 1
			
			# get a list of the neighbor attribute values [i][0] and user.id's [i][1]
			n = getNeighbors(dataset, userInstance, int(matchmakingInstance.k))
			print(n)
			
			# add all the neighbors to the matchmakingInstance of the user
			allNeighbors = []
			for i in range(int(matchmakingInstance.k)):
				neighbor = User.objects.get(id=n[i][1])
				allNeighbors.append(neighbor)
			matchmakingInstance.neighbors.add(*allNeighbors)
			
			try: 
				Matchmaking.objects.get(user=request.user)
				return redirect('matchmakingresults')
			except Matchmaking.DoesNotExist:
				return redirect('matchmakingindex')
			
	else:
		form = MatchmakingForm()

	context = {
		'form': form,
	}
	
	return render(request, 'matchmaking/index.html', context)
	
def results(request):
	result = get_object_or_404(Matchmaking, user=request.user)
	context = {
		'result': result,
	}
	return render(request, 'matchmaking/results.html', context)