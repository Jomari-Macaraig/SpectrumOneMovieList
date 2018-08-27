from django.urls import path

from .views import MovieList, MovieDetail

urlpatterns = [
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('list/', MovieList.as_view(), name='movie_list'),
]
