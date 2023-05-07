from django.db import models
from django.contrib.auth.models import AbstractUser


def profile_image_store(instance, filename):
    return f"profile/{instance.username}/{filename}"


class User(AbstractUser):
    profile_image = models.ImageField(upload_to=profile_image_store, default='profile/default.jpg')

    def __str__(self):
        return self.username


class Profile(models.Model):
    short_info = models.CharField(null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('app.FilmWork', related_name='profiles')

    def __str__(self):
        return self.user.username
