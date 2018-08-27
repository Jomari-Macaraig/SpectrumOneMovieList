from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Movie

class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
