from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse

from .models import Tournoi
from .models import Poule

def tournoi(request):
    tournois = get_list_or_404(Tournoi)
    return render(request,'tournois/tournoi.html',{'tournois':tournois})

def poules(request,tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    return render(request,'tournois/poule.html',{'tournoi':tournoi})

def matches(request,tournoi_id,poule_id):
    poule = get_object_or_404(Poule, pk=poule_id)
    points = poule.points()
    return render(request,'tournois/match.html',{'poule':poule,'points':points})
    
