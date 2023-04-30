from rest_framework import serializers

from . import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = '__all__'
    
    
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = '__all__'
