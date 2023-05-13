from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from django.utils import timezone

from . import models


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


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = '__all__'


class FilmWorkSerializer(serializers.ModelSerializer):
    rating = serializers.ReadOnlyField(source='get_rating')
    genres = GenreSerializer(many=True)
    persons = PersonSerializer(many=True)
    currency = CurrencySerializer()

    class Meta:
        model = models.FilmWork
        fields = '__all__'


class FilmWorkFirstSliderSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = models.FilmWork
        fields = [
            'id',
            'name',
            'backdrop',
            'slogan',
            'genres',
            'year',
            'age_rating'
        ]


class FilmWorkOtherSlidersSerializer(serializers.ModelSerializer):
    rating = serializers.ReadOnlyField(source='get_rating')

    class Meta:
        model = models.FilmWork
        fields = ['id', 'poster', 'name', 'rating']


class BrowsingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrowsingHistory
        fields = '__all__'
        read_only_fields = ['film_work', 'profile', 'watched_at']

    def create(self, validated_data):
        print(validated_data)
        try:
            return super().create(validated_data)
        except Exception as e:
            history = models.BrowsingHistory.objects.filter(
                film_work_id=validated_data['film_work_id'],
                profile=validated_data['profile']
            ).first()
            history['watched_at'] = timezone.now()
            history.save()
            return history


            
