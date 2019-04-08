from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic.base import RedirectView
from .models import *
from .forms import *

# Create your views here.
def index(request):
	
	if request.method == 'POST':
		form = MatchmakingForm(request.POST)  #<-- Note the extra arg
		if form.is_valid():
			matchmakingInstance = form.save(commit=False)
			if request.user.is_authenticated:
				matchmakingInstance.user = request.user
			else:
				matchmakingInstance.user = None
			matchmakingInstance.save()
			
			neighbor = User.objects.get(pk=3)
			matchmakingInstance.neighbors.add(neighbor)
			
	else:
		form = MatchmakingForm()

	context = {
		'form': form,
	}
	
	return render(request, 'matchmaking/index.html', context)