from django.db import models


class Restaurant(models.Model):
    """Restaurant model."""

    name = models.CharField(max_length=50)
    # Address
    rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    