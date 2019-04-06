from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from Users.forms import ProfileForm
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def profile(request, user_pk):
    profile = get_object_or_404(UserProfile, user = user_pk)

    context = {
        'profile':profile,
    }

    return render(request, 'User/Profile.html',context)

def EditProfile(request, user_pk):
    profile = get_object_or_404(UserProfile, user = user_pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = profile)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(pk = user_pk)
            post.save()
            return redirect('profile', user_pk = user_pk)
    else:
        form = ProfileForm(instance = post)


    context = {
        'profile':profile,
        'form':form,
    }

    return render (request, 'User/EditProfile.html',context)
# Create your views here.
