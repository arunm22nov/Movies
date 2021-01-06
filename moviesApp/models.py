from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your models here.


class genre(models.Model):
    genre_name = models.CharField(max_length=20)


class movies(models.Model):
    popularity = models.FloatField()
    director= models.CharField(max_length=70)
    genre_m = models.ManyToManyField(genre)
    imdb_score = models.FloatField()
    name= models.CharField(max_length=70)
    
    
    def get_genre(self):
        return ",".join([str(p.genre_name) for p in self.genre_m.all()])
    
    
 
