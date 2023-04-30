from django.urls import path

from . import views


urlpatterns = [
    path('movies/', views.MovieListCreateAPIView.as_view()),
    path('ratings/', views.RatingListCreateAPIView.as_view()),
    path('genres/', views.GenreListCreateAPIView.as_view()),
    path('persons/', views.PersonListCreateAPIView.as_view()),
    path('budgets/', views.BudgetListCreateAPIView.as_view()),
]
