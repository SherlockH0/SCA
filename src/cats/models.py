from typing import TYPE_CHECKING

from django.db import models

from cats.validators import validate_breed

if TYPE_CHECKING:
    from src.missions.models import Mission


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, validators=[validate_breed])
    years_of_experience = models.PositiveSmallIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    missions: models.Manager["Mission"]
