from rest_framework import serializers

from . import models


class MovieSerializer(serializers.ModelSerializer):
    model = models.Movie
    fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    model = models.Rating
    fields = '__all__'
    
class GenreSerializer(serializers.ModelSerializer):
    model = models.Genre
    fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    model = models.Person
    fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    model = models.Budget
    fields = '__all__'
