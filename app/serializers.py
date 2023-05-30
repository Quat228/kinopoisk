from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from django.utils import timezone
from django.db.utils import IntegrityError

from . import models
from accounts.serializers import ProfileSerializer
from accounts.models import User, Profile


def is_favorite_add(function):
    def wrap(self, instance):
        representation = function(self, instance)
        request = self.context.get('request')
        representation['is_favorite'] = False
        if not request.user.is_anonymous:
            representation['is_favorite'] = request.user.profile in instance.profiles.all()
        return representation
    return wrap


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = '__all__'
        read_only_fields = ['film_work', 'profile']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            new_rate = validated_data.pop('rate')
            instance = self.Meta.model.objects.get(**validated_data)
            instance.rate = new_rate
            instance.save()
            return instance


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
    reaction = serializers.ReadOnlyField(source='get_reaction')
    rating = serializers.ReadOnlyField(source='get_rating')
    rating_count = serializers.ReadOnlyField(source='get_rating_count')
    views_count = serializers.ReadOnlyField(source='get_views_count')
    genres = GenreSerializer(many=True)
    persons = PersonSerializer(many=True)
    currency = CurrencySerializer()

    class Meta:
        model = models.FilmWork
        fields = '__all__'

    @is_favorite_add
    def to_representation(self, instance):
        return super().to_representation(instance)


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

    @is_favorite_add
    def to_representation(self, instance):
        return super().to_representation(instance)


class FilmWorkFilterSerializer(serializers.ModelSerializer):
    rating = serializers.ReadOnlyField(source='get_rating')

    class Meta:
        model = models.FilmWork
        fields = ['id', 'poster', 'name', 'rating']

    @is_favorite_add
    def to_representation(self, instance):
        return super().to_representation(instance)


class BrowsingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrowsingHistory
        fields = '__all__'
        read_only_fields = ['film_work', 'profile', 'watched_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except Exception as e:
            history = models.BrowsingHistory.objects.filter(
                film_work_id=validated_data['film_work_id'],
                profile=validated_data['profile']
            ).first()
            history.watched_at = timezone.now()
            history.save()
            return history


class CommentSerializer(serializers.ModelSerializer):
    reaction = serializers.ReadOnlyField(source='get_reaction')

    class Meta:
        model = models.Comment
        fields = '__all__'
        read_only_fields = ['profile', 'film_work']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        profile = Profile.objects.get(id=representation['profile'])
        username = profile.user.username
        representation['username'] = username
        return representation

      
class ReactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReactionType
        fields = "__all__"


class FilmWorkReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilmWorkReaction
        fields = "__all__"
        read_only_fields = ['profile', 'film_work']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            new_reaction_type = validated_data.pop('reaction')
            instance = self.Meta.model.objects.get(**validated_data)
            instance.reaction = new_reaction_type
            instance.save()
            return instance


class CommentReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentReaction
        fields = "__all__"
        read_only_fields = ['profile', 'comment']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            new_reaction_type = validated_data.pop('reaction')
            instance = self.Meta.model.objects.get(**validated_data)
            instance.reaction = new_reaction_type
            instance.save()
            return instance
