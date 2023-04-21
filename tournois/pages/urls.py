from django.urls import path
from django.urls import include

from . import views

app_name = 'tournois'

urlpatterns = [
    path('', views.tournois, name='tournois'),
    path('<int:tournoi_id>/', views.tournoi, name = 'tournoi'),
    path('poule/<int:poule_id>/', views.poule, name = 'poule'),
    path('match/<int:match_id>/', views.match, name = 'match'),
    path('register/', views.register, name='register'),
    path('account/login/', views.login, name='login'),
    path('account/logout/', views.logout, name='logout'),
    
    # path('comment/<int:match_id>',views.match, name='comment'),
]