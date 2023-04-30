from django.urls import path

from . import views


urlpatterns = [
    path('movies/', views.MovieListCreateAPIView.as_view()),
    path('ratings/', views.MovieListCreateAPIView.as_view()),
]
