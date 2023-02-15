from django.db import models


class Restaurant(models.Model):
    """Restaurant model."""

    name = models.CharField(max_length=50)
    # Address
    rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    

class Meal(models.Model):
    """Meal model.
    Represents the meal that restaurant selling"""

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f'{self.restaurant} - {self.name}'
    
    # def get_abolute_url(self):
    #     pass
    