from django.urls import path

from .views import (
    MovieUpdateAPIView,
    MovieCreate,
    MovieUpdate,
    MovieDelete,
    MovieDetail,
    MovieList,
)

urlpatterns = [
    path('api/<int:pk>/update', MovieUpdateAPIView.as_view(), name='movie_api_update'),
    path('add/', MovieCreate.as_view(), name='movie_create'),
    path('<int:pk>/update', MovieUpdate.as_view(), name='movie_update'),
    path('<int:pk>/delete', MovieDelete.as_view(), name='movie_delete'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('list/', MovieList.as_view(), name='movie_list'),
]
