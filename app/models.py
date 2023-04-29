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
