from datetime import date, timezone
from django.db import models
from django.utils import timezone


class Tournoi(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
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
    
    def points(self):
        point = {}
        scored = {}
        conceded = {}
        for match in Match.objects.filter(poule=self):
            if match.score1 > match.score2:   #equipe1 wins
                scored[match.equipe1.id] = scored.get(match.equipe1.id, 0) + match.score1  
                conceded[match.equipe1.id] = conceded.get(match.equipe1.id, 0) + match.score2
                scored[match.equipe2.id] = scored.get(match.equipe2.id, 0) + match.score2
                conceded[match.equipe2.id] = conceded.get(match.equipe2.id, 0) + match.score1
                point[match.equipe1.id] = point.get(match.equipe1.id, 0) + 3
            elif match.score1 == match.score2:
                scored[match.equipe1.id] = scored.get(match.equipe1.id, 0) + match.score1
                conceded[match.equipe1.id] = conceded.get(match.equipe1.id, 0) + match.score2
                scored[match.equipe2.id] = scored.get(match.equipe2.id, 0) + match.score2
                conceded[match.equipe2.id] = conceded.get(match.equipe2.id, 0) + match.score1
                point[match.equipe1.id] = point.get(match.equipe1.id, 0) + 1
                point[match.equipe2.id] = point.get(match.equipe2.id, 0) + 1
            elif match.score1 < match.score2: #equipe1 loses
                scored[match.equipe1.id] = scored.get(match.equipe1.id, 0) + match.score1
                conceded[match.equipe1.id] = conceded.get(match.equipe1.id, 0) + match.score2
                scored[match.equipe2.id] = scored.get(match.equipe2.id, 0) + match.score2
                conceded[match.equipe2.id] = conceded.get(match.equipe2.id, 0) + match.score1
                point[match.equipe2.id] = point.get(match.equipe2.id, 0) + 3
        # make a rank of teams first by points and second by recorded, third by conceded
        length = len(point)
        points = {} 
        for i in range(length):
            k_n = [(k,v) for k,v in point.items()][0][0] # key to compare
            for k,v in point.items():
                if v > point.get(k_n):
                    k_n = k 
                elif v == point.get(k_n):
                    if scored.get(k) > scored.get(k_n):
                        k_n = k
                    elif  scored.get(k) == scored.get(k_n):
                        if conceded.get(k) < conceded.get(k):
                            k_n = k
            points[Equipe.objects.get(pk=k_n).name] = [point.get(k_n), scored.get(k_n), conceded.get(k_n)]
            point.pop(k_n)
        return points
        
                
class Match(models.Model):
    time = models.DateTimeField(null=True)
    location = models.CharField(max_length=200)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    equipe1 = models.ForeignKey('Equipe',on_delete=models.CASCADE,related_name='equipe01',null=True)
    equipe2 = models.ForeignKey('Equipe',on_delete=models.CASCADE,related_name='equipe02',null=True)
    poule = models.ForeignKey('Poule',on_delete=models.CASCADE,null=True)
    
    
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
    
    

    
    
    
    
    
