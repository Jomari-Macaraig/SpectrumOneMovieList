from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .mixins import MovieActionMixin
from .models import Movie


class MovieCreate(MovieActionMixin, CreateView):
    model = Movie
    fields = ['title']
    action_past_tense = 'created'
    template_name = 'movie/movie_create_form.html'


class MovieUpdate(MovieActionMixin, UpdateView):
    model = Movie
    fields = ['title']
    action_past_tense = 'updated'
    template_name = 'movie/movie_update_form.html'


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'


class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
