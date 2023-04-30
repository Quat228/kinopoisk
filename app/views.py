from rest_framework import generics

from . import models
from . import serializers


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.GenreSerializer


class BudgetListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Budget.objects.all()
    serializer_class = serializers.BudgetSerializer
