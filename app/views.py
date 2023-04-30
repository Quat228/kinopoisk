from rest_framework import generics

from . import models
from . import serializers


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class RatingListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
