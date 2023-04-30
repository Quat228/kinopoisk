from rest_framework import serializers

from . import models


class SerializerMovie(serializers.ModelSerializer):
    model = models.Movie
    fields = "__all__"


class SerializerRating(serializers.ModelSerializer):
    model = models.Rating
    fields = "__all__"
