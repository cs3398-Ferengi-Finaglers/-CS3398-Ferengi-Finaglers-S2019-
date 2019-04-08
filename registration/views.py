from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect



def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data['password1'])
			#messages.success(request, 'Account created for {username}!')
			#login(request, user)
			return HttpResponseRedirect("http://127.0.0.1:8000/questionnaire/1")
	else:
		form = UserRegisterForm()
	return render(request, 'registration/register.html', {'form': form})

class login(LoginView):
	template_name='registration/login.html'

