from django.db import models
from django.contrib.auth.models import AbstractUser


def profile_image_store(instance, filename):
    return f"profile/{instance.username}/{filename}"


class User(AbstractUser):
    profile_image = models.ImageField(upload_to=profile_image_store, default='profile/default.jpg')
    email = models.EmailField("email address", blank=True, unique=True, null=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    short_info = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorites = models.ManyToManyField('app.FilmWork', related_name='profiles')

    def __str__(self):
        return self.user.username
