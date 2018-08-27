from django.views.generic import ListView
from django.shortcuts import render

from .models import Movie

class MovieList(ListView):
    model = Movie
    template_name = 'movie/movielist.html'
