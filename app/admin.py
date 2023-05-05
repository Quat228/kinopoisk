from django.contrib import admin

from . import models


admin.site.register(models.FilmWork)
admin.site.register(models.Rating)
admin.site.register(models.Genre)
admin.site.register(models.Person)
admin.site.register(models.Currency)
