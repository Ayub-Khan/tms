"""Models for our database."""

from django.db import models

# Create your models here.


class Client(models.Model):
    """Client model."""

    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        """Stringify function."""
        return self.name

    objects = models.Manager()
