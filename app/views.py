from rest_framework import generics

from . import models
from . import serializers


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class RatingListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class BudgetListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Budget.objects.all()
    serializer_class = serializers.BudgetSerializer
