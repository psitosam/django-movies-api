from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie 

# data = {
#   'movies': [
#     {
#       'id': 29,
#       'title': 'Jaws',
#       'year': 1975
#     },
#     {
#       'id': 30,
#       'title': 'Sharknado',
#       'year': 2013
#     },
#     {
#       'id': 31,
#       'title': 'The Meg',
#       'year': 2018
#     }
#   ]
# }

def movies(request):
  data = Movie.objects.all()
  return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("Home page")

def detail(request, id):
  data = Movie.objects.get(pk=id)
  return render(request, 'movies/detail.html', {'movie': data})