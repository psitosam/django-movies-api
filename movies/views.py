from http.client import HTTPResponse


from django.http import HttpResponse
from django.shortcuts import render

data = {
  'movies': [
    {
      'id': 29,
      'title': 'Jaws',
      'year': 1975
    },
    {
      'id': 30,
      'title': 'Sharknado',
      'year': 2013
    },
    {
      'id': 31,
      'title': 'The Meg',
      'year': 2018
    }
  ]
}

def movies(request):
  return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home page")