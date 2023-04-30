from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenreListCreateAPIView.as_view()),
    path('persons/', views.PersonListCreateAPIView.as_view()),
    path('budgets/', views.BudgetListCreateAPIView.as_view()),
]
