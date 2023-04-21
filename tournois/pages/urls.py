from django.urls import path

from . import views

app_name = 'tournois'

urlpatterns = [
    path('', views.tournois, name='tournois'),
    path('<int:tournoi_id>/', views.tournoi, name = 'tournoi'),
    path('poule/<int:poule_id>/', views.poule, name = 'poule'),
    path('match/<int:match_id>/', views.match, name = 'match'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]