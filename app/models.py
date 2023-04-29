from django.db import models


class Movie(models.Model):
    backdrop = models.URLField()
    movie_length = models.IntegerField()
    companies = models.ManyToManyField("Company", related_name='movies')
    type = models.CharField(max_length=30)
    name = models.CharField()
    description = models.TextField()
    premiere = models.DateTimeField
    slogan = models.CharField()
    year = models.IntegerField()
    budget = models.ForeignKey("Budget", on_delete=models.CASCADE, related_name='movies')
    poster = models.URLField()
    genres = models.ManyToManyField("Genre", related_name='movies')
    trailer_url = models.URLField()
    persons = models.ManyToManyField("Person", related_name='movies')
    age_rating = models.IntegerField(default=18)
    top10 = models.BooleanField(null=True)
    top250 = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=45)
    url = models.URLField()
    preview_url = models.URLField(null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Person(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=55)
    profession = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Budget(models.Model):
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.currency
        