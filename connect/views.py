from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
try:
    from django.contrib.auth import get_user_model
    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
    user_model = User
from django.shortcuts import render, get_object_or_404, redirect

from connect.exceptions import AlreadyExistsError
from connect.models import Friend, FriendshipRequest
from Users.models import UserProfile

get_friendship_context_object_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_NAME', 'user')
get_friendship_context_object_list_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME', 'users')



# Create your views here.
def home_view(request, *args, **kwargs):
	if request.method == "POST":
		if 'sendRequest' in request.POST:
			sendRequest= request.POST.get("sendRequest")
			other_user = User.objects.get(pk=sendRequest)
			Friend.objects.add_friend(
    			sendRequest,                               # The sender
    			other_user)
			#friendship_add_friend(request, sendRequest)
		elif 'acceptRequest' in request.POST:
			accept= request.POST.get("acceptRequest")
			friend_request = FriendshipRequest.objects.get(from_user=accept)
			friend_request.accept()
			#friendship_accept(request, accept)
		elif 'rejectRequest' in request.POST:
			reject= request.POST.get("rejectRequest")
			friend_request = FriendshipRequest.objects.get(from_user=reject)
			friend_request.reject()
			#friendship_reject(request, reject)
#			FriendRequests.objects.filter(user=request.user, request= myFriend).update(friendship=True)
		return HttpResponseRedirect("/AddFriends")
	else:
		my_request = FriendshipRequest.objects.filter(to_user=request.user)
		#for i in my_request:
		#	profile = [get_object_or_404(UserProfile, user = i.from_user.id)]
		myuser = User.objects.all()
		my_context = {
			"my_request": my_request,
			"myuser": myuser,
			#"profile": profile
		}
		return render(request, "connect/connect.html", my_context)