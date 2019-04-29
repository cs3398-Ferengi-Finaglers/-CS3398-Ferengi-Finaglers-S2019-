from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from Users.forms import ProfileForm
from Matchmaking.forms import UserRatingForm
from Matchmaking.models import UserRating
from connect.exceptions import AlreadyExistsError
from connect.models import Friend, FriendshipRequest

@login_required(login_url='/login/')
def profile(request, user_pk):
    profile = get_object_or_404(UserProfile, user = user_pk)
    
    if request.method == 'POST':
        if 'addFriend' in request.POST:
            sendRequest= request.POST.get("addFriend")
            other = User.objects.get(pk=sendRequest)
            Friend.objects.add_friend(
                request.user,                               # The sender
                other)
        ratingForm = UserRatingForm(request.POST)
        if ratingForm.is_valid():
            UserRating.objects.filter(userDoingTheRating=request.user).delete() #delete past rating/refresh response
            ratingInstance = ratingForm.save(commit=False)
            if request.user.is_authenticated:
                ratingInstance.userDoingTheRating = request.user
            else:
                ratingInstance.userDoingTheRating = None
            ratingInstance.userBeingRated = User.objects.get(pk=user_pk)
            ratingInstance.save()
    else:
        ratingForm = UserRatingForm()
		
    context = {
        'profile':profile,
        'ratingForm':ratingForm,
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
        form = ProfileForm(instance = profile)


    context = {
        'profile':profile,
        'form':form,
    }

    return render (request, 'User/EditProfile.html',context)

# Create your views here.
