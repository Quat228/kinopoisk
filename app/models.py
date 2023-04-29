from django.db import models as m


class Company(m.Model):
    name = m.CharField(max_length=45)
    url = m.URLField()
    preview_url = m.URLField(null=True)

    def __str__(self):
        return self.name


class Genre(m.Model):
    name = m.CharField(max_length=25)

    def __str__(self):
        return self.name


class Person(m.Model):
    photo = m.ImageField()
    name = m.CharField(max_length=55)
    profession = m.CharField(max_length=55)

    def __str__(self):
        return self.name


class Budget(m.Model):
    currency = m.CharField(max_length=2)

    def __str__(self):
        return self.currency
