from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=150)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    isbn = models.CharField(max_length=13, unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title