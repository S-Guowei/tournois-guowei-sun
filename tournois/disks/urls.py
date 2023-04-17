from django.urls import path

from . import views

app_name = 'disks'

urlpatterns = [
    path('', views.tournois, name='tournois'),
    path('<int:tournoi_id>/',views.poules, name='poules')

]