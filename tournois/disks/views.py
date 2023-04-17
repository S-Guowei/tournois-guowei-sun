from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse

from .models import Tournoi

def tournois(request):
    tournois = get_list_or_404(Tournoi)
    return render(request,'disks/tournois.html',{'tournois':tournois})

def poules(request,tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    return render(request,'disks/poules.html',{'tournoi':tournoi})
    
