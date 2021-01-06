from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serialize import MoviesSeriealize
from .models import movies ,genre
import json
from django.conf import settings
import requests
#https://arun-movies.herokuapp.com/
BASE_URL="http://127.0.0.1:8000"

@api_view(["GET"])
def getMoviesList(request):
    movies_list = None 
    movies_list=movies.objects.all().order_by('name')
    if movies_list.count() < 100:
        setDefaultMoviesList();
        movies_list=movies.objects.all().order_by('name')
        
    data = MoviesSeriealize(movies_list, many=True)
    
    return JsonResponse(data.data,safe=False)


def movie_display(request):
    req = requests.get((BASE_URL +"/get_movies/"), params=request.GET)
    mov=None
    if req.status_code == 200:
        mov=req.json()
        
    if request.method == 'GET' and request.GET.get('form_type')=='formOne':
        user_input=request.GET.get('search')
        key=request.GET.get('Company')
    return render(request, 'movies.html', {'movies_list': mov})
    #JsonResponse(r.json(), safe=False)
    #

def filter_movies(request):
    req = requests.get((BASE_URL +"/get_movies/"), params=request.GET)
    if req.status_code == 200:
        mov=req.json()
    user_input = request.GET.get('inputValue')
    key=request.GET.get('searchtype')
    if key == "genre":
        value=list(filter(lambda x: [j for j in [i['genre_name'].strip().lower() for i in x['genre_m']] if user_input.lower() in j],mov))
        #value=list(filter(lambda x: user_input.lower() in x['genre_m'][0]['genre_name'].lower(),mov))
    elif key=="" or key is None or user_input=='' or user_input is None:
        value=mov
    else:
          
        value=list(filter(lambda x:user_input.lower() in x[key].lower(), mov ))
    data = {'response': value}
    return JsonResponse(data)





def setDefaultMoviesList():
    json_data = open((str(settings.BASE_DIR) +'/static/imdb.json'))
    data1 =json.load(json_data)
    

    for i in data1:
            # c = signup_model.objects.create(user_name="nmghfhf15@gmail.com", first_name='ggggg', password="12345")
        usr = movies.objects.create(popularity=float(i['99popularity']), director=i['director'],
                                        imdb_score=float(i['imdb_score']),
                                        name=i['name'])
        for j in i['genre']:
            gnexists = genre.objects.filter(genre_name=j)
            if gnexists.exists():
                gn = genre.objects.get(id=gnexists[0].id)
                gn.movies_set.add(usr)
            else:
                gn = genre.objects.create(genre_name=j)
                gn.movies_set.add(usr)