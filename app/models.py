from django.db import models

from accounts.models import Profile


class FilmWork(models.Model):
    backdrop = models.URLField()
    movie_length = models.IntegerField()
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    description = models.TextField()
    premiere = models.DateTimeField()
    slogan = models.CharField(max_length=100, null=True)
    year = models.IntegerField()
    budget = models.IntegerField(default=0)
    currency = models.ForeignKey("Currency", on_delete=models.SET_NULL, related_name='film_works', null=True)
    poster = models.URLField()
    genres = models.ManyToManyField("Genre", related_name='film_works')
    trailer_url = models.URLField()
    persons = models.ManyToManyField("Person", related_name='film_works')
    age_rating = models.IntegerField(default=18)
    top10 = models.BooleanField(null=True)
    top250 = models.BooleanField(null=True)

    def get_rating(self):
        queryset = self.ratings.all()
        rates = []
        for obj in queryset:
            rates.append(obj.rate)

        return sum(rates) / len(rates) if rates else 0.0

    def get_rating_count(self):
        queryset = self.ratings.all()
        return len(queryset)

    def get_views_count(self):
        queryset = self.browsing_histories.all()
        return len(queryset)

    def __str__(self):
        return self.name


class Rating(models.Model):
    film_work = models.ForeignKey("FilmWork", related_name='ratings', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='ratings', on_delete=models.CASCADE)
    rate = models.FloatField(choices=[
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ])

    class Meta:
        unique_together = ['film_work', 'profile']

    def __str__(self):
        return f"{self.film_work.name} | {self.rate} | {self.profile}"


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


class Currency(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class BrowsingHistory(models.Model):
    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE, related_name='browsing_histories')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='browsing_histories')
    watched_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['film_work', 'profile']

    def __str__(self):
        return f"{self.film_work} - {self.profile} | {self.watched_at}"
