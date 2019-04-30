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
    friends = Friend.objects.friends(request.user)
    my_request = FriendshipRequest.objects.filter(to_user=request.user).values_list('from_user', flat=True).order_by('id')
    sent_requests=FriendshipRequest.objects.filter(from_user=request.user).values_list('to_user', flat=True).order_by('id')
    
    if request.method == 'POST':
        if 'sendRequest' in request.POST:
            sendRequest= request.POST.get("sendRequest")
            other_user = User.objects.get(pk=sendRequest)
            Friend.objects.add_friend(
                request.user,                              
                other_user)
        elif 'acceptRequest' in request.POST:
            accept= request.POST.get("acceptRequest")
            friend_request = FriendshipRequest.objects.get(from_user=accept)
            friend_request.accept()
        elif 'rejectRequest' in request.POST:
            reject= request.POST.get("rejectRequest")
            friend_request = FriendshipRequest.objects.get(from_user=reject)
            friend_request.reject()
        elif 'deleteFriend' in request.POST:
            remove = request.POST.get("deleteFriend")
            remove_user = User.objects.get(pk=remove);
            Friend.objects.remove_friend(
                request.user,                               
                remove_user)
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
            'friends': friends,
            'my_request': my_request,
            'sent_requests': sent_requests,
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
