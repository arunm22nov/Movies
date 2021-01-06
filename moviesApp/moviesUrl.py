'''
Created on 03-Jan-2021

@author: arun
'''
from django.urls import path
from . import views


urlpatterns=[path('movies/',views.movie_display),
             path('get_movies/',views.getMoviesList),
             path('get_response/', views.filter_movies, name='get_response')
    
    ]