from django.urls import path

from .views import MovieCreate, MovieDetail, MovieList

urlpatterns = [
    path('add/', MovieCreate.as_view(), name='movie_create'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('list/', MovieList.as_view(), name='movie_list'),
]
