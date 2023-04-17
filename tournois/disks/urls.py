from django.urls import path

from . import views

app_name = 'tournois'

urlpatterns = [
    path('', views.tournois, name='tournois'),
    path('<int:tournoi_id>/',views.poules, name='poules'),
    path('<int:tournoi_id>/<int:poule_id>/',views.matches,name = 'matches')

]