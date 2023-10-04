from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )
    description = models.CharField(
        blank=True,
        max_length=120,
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(0, "Number has to be more than or equal to 0"),
                    MaxValueValidator(101,"Number has to be 100 or less"),]
        
    )
