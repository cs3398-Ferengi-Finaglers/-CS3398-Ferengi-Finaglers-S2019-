from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import FriendRequests
from .forms import SendForm

# Create your views here.
def home_view(request, *args, **kwargs):
	if request.method == "POST":
		if 'sendRequest' in request.POST:
			formOne = SendForm(request.POST)
			if formOne.is_valid():
				print(formOne.cleaned_data['Select_New_Friend'])
#				myFriend = FriendRequests.objects.filter(user=newFriend)
#				print(myFriend)
#				FriendRequests.objects.filter(user=request.user).update(request = newFriend)

		elif 'addFriend' in request.POST:
			myFriend = request.POST.get("addFriend", "")
			print(myFriend)
#			FriendRequests.objects.filter(user=request.user, request= myFriend).update(friendship=True)
		return HttpResponseRedirect("/AddFriends")
	else:
		#requests = FriendRequests.objects.filter(user=request.user, friendship=False).values("request").values_list('request')
		requests = FriendRequests.objects.filter(friendship=False, user=request.user)
		form1 = User.objects.all()
		my_context = {
			"form2": requests,
			"form1": form1
		}
		return render(request, "connect/connect.html", my_context)



