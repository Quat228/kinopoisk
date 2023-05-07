from django.urls import path

from . import views


urlpatterns = [
    path('filmworks/', views.FilmWorkListAPIView.as_view()),
    
    path('filmworks/new/', views.FilmWorkListMovieCartoonNew.as_view()),
    path('filmworks/horror/', views.FilmWorkListMovieCartoonHorror.as_view()),
    path('filmworks/family/', views.FilmWorkListMovieCartoonFamily.as_view()),
    
    path('filmworks/movie/new/', views.FilmWorkListNewMovieAPIView.as_view()),
    path('filmworks/movie/horror/', views.FilmWorkListFamilyMovieAPIView.as_view()),
    path('filmworks/movie/family/', views.FilmWorkListHorrorMovieAPIView.as_view()),

    path('filmworks/cartoon/new/', views.FilmWorkListNewCartoonAPIView.as_view()),
    path('filmworks/cartoon/horror/', views.FilmWorkListFamilyCartoonAPIView.as_view()),
    path('filmworks/cartoon/family/', views.FilmWorkListHorrorCartoonAPIView.as_view()),
    
    path('filmworks/<int:pk>', views.FilmWorkRetrieveUpdateDestroyAPIView.as_view()),


    path('ratings/', views.RatingListAPIView.as_view()),

    path('genres/', views.GenreListAPIView.as_view()),

    path('persons/', views.PersonListAPIView.as_view()),

    path('budgets/', views.CurrencyListAPIView.as_view()),


    path('filmworks/<int:pk>', views.FilmWorkRetrieveUpdateDestroyAPIView.as_view()),
]
