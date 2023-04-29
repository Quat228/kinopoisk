from django.db import models


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
    currency = models.CharField(max_length=2)

    def __str__(self):
        return self.currency
