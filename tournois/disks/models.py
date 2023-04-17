from datetime import date, timezone
from django.db import models
from django.utils import timezone


class Tournoi(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    
    def __str__(self):
        return self.name
    
class Poule(models.Model):

    number = models.CharField(max_length=20,default=0)
    tournoi = models.ForeignKey('Tournoi',on_delete=models.CASCADE)
    equipes = models.ManyToManyField('Equipe')
    
    def __str__(self):
        return self.tournoi.name+', poule'+self.number
    
class Match(models.Model):
    time = models.DateTimeField(null=True)
    place = models.CharField(max_length=200)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    equipe1 = models.ForeignKey('Equipe',on_delete=models.CASCADE,related_name='equipe01',null=True)
    equipe2 = models.ForeignKey('Equipe',on_delete=models.CASCADE,related_name='equipe02',null=True)
    
    
    def __str__(self):
        return self.equipe1.name+" vs "+self.equipe2.name
    
    
class Equipe(models.Model):
    name = models.CharField(max_length=200)
    coach_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
      
class Player(models.Model):
    name = models.CharField(max_length=200)
    equipe = models.ForeignKey('Equipe',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name
    
    

    
    
    
    
    
