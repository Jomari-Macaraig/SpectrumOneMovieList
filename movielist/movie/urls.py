from django.urls import path

from .views import MovieCreate, MovieUpdate, MovieDetail, MovieList

urlpatterns = [
    path('add/', MovieCreate.as_view(), name='movie_create'),
    path('update/<int:pk>/', MovieUpdate.as_view(), name='movie_update'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('list/', MovieList.as_view(), name='movie_list'),
]
