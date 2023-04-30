from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Movie(models.Model):
    backdrop = models.URLField()
    movie_length = models.IntegerField()
    type = models.CharField(max_length=30)
    name = models.CharField()
    description = models.TextField()
    premiere = models.DateTimeField()
    slogan = models.CharField(null=True)
    year = models.IntegerField()
    value = models.IntegerField(default=0)
    budget = models.ForeignKey("Budget", on_delete=models.CASCADE, related_name='movies')
    poster = models.URLField()
    genres = models.ManyToManyField("Genre", related_name='movies')
    trailer_url = models.URLField()
    persons = models.ManyToManyField("Person", related_name='movies')
    age_rating = models.IntegerField(default=18)
    top10 = models.BooleanField(null=True)
    top250 = models.BooleanField(null=True)

    def get_rating(self):
        queryset = self.ratings.all()
        rate = []
        for obj in queryset:
            rate.append(obj.rate)

        return sum(rate) / len(rate)

    def __str__(self):
        return self.name


class Rating(models.Model):
    movie = models.ForeignKey("Movie", related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    rate = models.FloatField(choices=[
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ])

    def __str__(self):
        return f"{self.movie.name}|{self.rate}"


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Person(models.Model):
    photo = models.URLField()
    name = models.CharField(max_length=55)
    profession = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Budget(models.Model):
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.currency
        