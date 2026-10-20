from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    categories = models.ManyToManyField(
        Category,
        related_name='tours'
    )

    def __str__(self):
        return self.title


class Ticket(models.Model):
    ticket_number = models.CharField(
        max_length=20,
        unique=True
    )

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    tour = models.OneToOneField(
        Tour,
        on_delete=models.CASCADE,
        related_name='ticket'
    )

    def __str__(self):
        return self.ticket_number


class Comment(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person} - {self.tour}"
