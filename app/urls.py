from django.urls import path

from . import views


urlpatterns = [
    path('filmworks/', views.FilmWorkListAPIView.as_view()),
    path('filmworks/firstslider/', views.FilmWorkListFirstSlider.as_view()),
    path('filmworks/otherslider/', views.FilmWorkListOtherSlider.as_view()),
    path('filmworks/search/', views.FilmWorkSearchAPIView.as_view()),

    path('filmworks/<int:pk>/', views.FilmWorkRetrieveAPIView.as_view()),
    path('filmworks/<int:pk>/history/', views.BrowsingHistoryCreateAPIView.as_view()),

    path('filmworks/<int:film_work_id>/comment/', views.CommentListCreateAPIView.as_view()),
    path('filmworks/<int:film_work_id>/comment/<int:pk>', views.CommentRetrieveUpdateDestroyAPIView.as_view()),

    path('filmworks/<int:film_work_id>/rating/', views.RatingCreateAPIView.as_view()),
    path('filmworks/popular/', views.FilmWorkPopularListAPIView.as_view()),
    path('filmworks/recommend/', views.FilmWorkRecommendListAPIView.as_view()),

    path('add/favorite/', views.FavoritesAddAPIView.as_view()),

    path('ratings/', views.RatingListAPIView.as_view()),

    path('genres/', views.GenreListAPIView.as_view()),

    path('persons/', views.PersonListAPIView.as_view()),

    path('budgets/', views.CurrencyListAPIView.as_view()),
]
