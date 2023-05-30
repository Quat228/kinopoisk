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
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, related_name='film_works')
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
        return sum(queryset)

    def get_reaction(self):
        reactions = self.reactions.all()
        result = {}
        for reaction in reactions:
            if result.get(reaction.reaction.name):
                result[reaction.reaction.name] += 1
            else:
                result[reaction.reaction.name] = 1

        return result

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

    def get_reaction(self):
        reactions = self.comment_reactions.all()
        result = {}
        for reaction in reactions:
            if result.get(reaction.reaction.name):
                result[reaction.reaction.name] += 1
            else:
                result[reaction.reaction.name] = 1

        return result

    def __str__(self):
        return self.text


class BrowsingHistory(models.Model):
    film_work = models.ForeignKey(FilmWork, on_delete=models.PROTECT, related_name='browsing_histories')
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='browsing_histories')
    watched_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['film_work', 'profile']

    def __str__(self):
        return f"{self.film_work} - {self.profile} | {self.watched_at}"


class ReactionType(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class FilmWorkReaction(models.Model):
    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE, related_name='reactions')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reaction = models.ForeignKey(ReactionType, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f'{self.film_work} - {self.profile} - {self.reaction}'

    class Meta:
        unique_together = ['film_work', 'profile']


class CommentReaction(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_reactions')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reaction = models.ForeignKey(ReactionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        unique_together = ['profile', 'comment']
