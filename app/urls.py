from django.urls import path

from . import views


urlpatterns = [
    path('filmworks/', views.FilmWorkListAPIView.as_view()),
    path('filmworks/firstslider/', views.FilmWorkListFirstSlider.as_view()),
    path('filmworks/filter/', views.FilmWorkFilterListAPIView.as_view()),
    path('filmworks/search/', views.FilmWorkSearchAPIView.as_view()),

    path('filmworks/<int:pk>/', views.FilmWorkRetrieveAPIView.as_view()),
    path('filmworks/<int:film_work_id>/reaction', views.FilmWorkReactionCreateAPIView.as_view()),
    path('filmworks/<int:pk>/history/', views.BrowsingHistoryCreateAPIView.as_view()),

    path('filmworks/<int:film_work_id>/comment/', views.CommentListCreateAPIView.as_view()),
    path('filmworks/<int:film_work_id>/comment/<int:pk>', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('filmworks/<int:film_work_id>/comment/<int:comment_id>/reaction', views.CommentReactionCreateAPIView.as_view()),

    path('filmworks/<int:film_work_id>/rating/', views.RatingCreateAPIView.as_view()),

    path('add/favorite/', views.FavoritesAddAPIView.as_view()),

    path('ratings/', views.RatingListAPIView.as_view()),

    path('genres/', views.GenreListAPIView.as_view()),

    path('persons/', views.PersonListAPIView.as_view()),

    path('budgets/', views.CurrencyListAPIView.as_view()),
]
