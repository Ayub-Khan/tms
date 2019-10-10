"""Models for client application."""

from django.db import models


class Client(models.Model):
    """Client model."""

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=18)
    gender = models.CharField(
        max_length=2,
        choices=[('M', 'Male'), ('F', 'Female'), ('Ot', 'Other')]
    )
    address = models.TextField(max_length=500)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        """Convert object to string having all fields data separated by _."""
        return 'name({})_email({})_phone({})'.format(
            self.name,
            self.email,
            self.phone_number
        )

    objects = models.Manager()
