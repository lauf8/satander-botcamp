from django.db import models

class Nationality(models.Model):
    nationality = models.CharField(max_length=75)
    
    def __str__(self):
        return self.nationality

class Sport(models.Model):
    sport = models.CharField(max_length=75)
    def __str__(self):
        return self.sport

class Athletes(models.Model):
    name = models.CharField(max_length=75) 
    age = models.IntegerField()
    ht = models.IntegerField()
    kg = models.IntegerField()
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
