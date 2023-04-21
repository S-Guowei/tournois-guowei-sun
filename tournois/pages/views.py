from django.shortcuts import render,get_list_or_404,get_object_or_404,redirect
from django.contrib.auth import authenticate

from .forms import LoginForm

from .models import Tournoi
from .models import Poule
from .models import Match
from .models import User

import hashlib

def tournois(request):
    tournois = get_list_or_404(Tournoi)
    
    return render(request,'tournois/tournois.html',{'tournois':tournois})

def tournoi(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    
    return render(request,'tournois/tournoi.html',{'tournoi':tournoi})

def poule(request, poule_id):
    poule = get_object_or_404(Poule, pk=poule_id)
    points = poule.points()
    
    return render(request,'tournois/poule.html',{'poule':poule,'points':points})

def match(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    
    return render(request,'tournois/match.html',{'match':match})



 
def register(request):
    pass
    
    return render(request,"tournois/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password', None)
        if username and password:  # make username and passwords are not null
            username = username.strip()
            # more other verifications.....
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    return redirect('/tournois/')
                else:
                    message = "password incorrect"
            except:
                message = "User not exists"
            return render(request, 'tournois/login.html',{'message':message})
            
    return render(request, 'tournois/login.html')

def logout(request):
    # response=HttpResponseRedirect('')
    # response.delete_cookie("username")
    pass
    return redirect('')