from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	#return HttpResponse("Hello world! You are now inside one of django's views.")
	return render(request, 'landing/index.html')