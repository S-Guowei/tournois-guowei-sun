from django.shortcuts import render,get_list_or_404,get_object_or_404,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .forms import CommentForm

from .models import Tournoi
from .models import Poule
from .models import Match


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

    # next = request.GET.get('next', '')

    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']

    #         user = auth.authenticate(username=username, password=password)

    #         if user is not None and user.is_active:
    #             auth.login(request, user)
    #             if  next == "":
    #                 return HttpResponseRedirect(reverse('tournois:tournois', args=[user.id]))
    #             else:
    #                 return HttpResponseRedirect(next)

    #         else:
                
    #            return render(request, 'login', {'form': form,})
    # else:
    #     form = LoginForm()
    pass

    return render(request, 'tournois/tournois.html')

def logout(request):

    pass
    return redirect('/tournois/')

    
