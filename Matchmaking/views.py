from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic.base import RedirectView
from .models import *
from .forms import *

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
			allNeighbors = []
			for i in range(1, int(matchmakingInstance.k) + 1):
				neighbor = User.objects.get(pk=i)
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