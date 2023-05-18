from django.contrib import admin

from . import models


@admin.register(models.FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BrowsingHistory)
class BrowsingHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
