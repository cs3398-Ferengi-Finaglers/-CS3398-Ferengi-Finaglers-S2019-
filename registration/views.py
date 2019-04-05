from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
    # return HttpResponse('<h3>Under Construction</h3>')
