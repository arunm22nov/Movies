'''
Created on 31-Dec-2020

@author: aruns
'''
from rest_framework import serializers

from .models import movies,genre

class GenreSeriealize(serializers.ModelSerializer):
    class Meta:
        model=genre
        fields='__all__'
        
class MoviesSeriealize(serializers.ModelSerializer):
    genre_m=GenreSeriealize(many=True)
    class Meta:
        model=movies
        fields=['popularity','director','name','imdb_score','genre_m']
        