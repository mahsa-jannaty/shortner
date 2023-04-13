from django.db import models

# Create your models here.
class ShortenedLink(models.Model):
    full_link = models.CharField(max_length = 20)
    short_link = models.CharField(max_length = 6)

    def __str__(self):
        return self.full_link