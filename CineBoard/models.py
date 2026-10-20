from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# Create your models here.
