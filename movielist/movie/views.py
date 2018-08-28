from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'


class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
