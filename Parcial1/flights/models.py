
from django.db import models

class Flight(models.Model):
    NATIONAL = 'N'
    INTERNATIONAL = 'I'
    FLIGHT_TYPE_CHOICES = [
        (NATIONAL, 'Nacional'),
        (INTERNATIONAL, 'Internacional'),
    ]

    name = models.CharField(max_length=100)
    flight_type = models.CharField(
        max_length=1,
        choices=FLIGHT_TYPE_CHOICES,
        default=NATIONAL,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name