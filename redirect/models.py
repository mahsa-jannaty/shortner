from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShortenedLink(models.Model):
    full_link = models.CharField(max_length=20)
    short_link = models.CharField(max_length=6)

    def __str__(self):
        return self.full_link


class FullLink(models.Model):
    full_link = models.CharField(max_length=100)


class ShortLink(models.Model):
    full_link = models.ForeignKey(FullLink, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    short = models.CharField(max_length=20)


