from django.urls import path

from . import views


urlpatterns = [
    path('movies/', views.FilmWorkListCreateAPIView.as_view()),
    path('ratings/', views.RatingListAPIView.as_view()),
    path('genres/', views.GenreListAPIView.as_view()),
    path('persons/', views.PersonListAPIView.as_view()),
    path('budgets/', views.CurrencyListAPIView.as_view()),

    path('movies/<int:pk>', views.FilmWorkRetrieveUpdateDestroyAPIView.as_view()),
]
