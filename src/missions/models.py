from django.db import models

from cats.models import Cat


class Mission(models.Model):
    cat = models.ForeignKey(
        Cat, on_delete=models.CASCADE, null=True, related_name="missions"
    )
    complete = models.BooleanField()

    targets: models.Manager["Target"]


class Target(models.Model):
    mission = models.ForeignKey(
        "missions.Mission", on_delete=models.CASCADE, related_name="targets"
    )
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    complete = models.BooleanField()
