from rest_framework import serializers

from . import models


class GenreSerializer(serializers.ModelSerializer):
    model = models.Genre
    fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    model = models.Person
    fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    model = models.Budget
    fields = '__all__'
