from statistics import mode
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Company(models.Model):
    datetime_created = models.DateTimeField()
    headline = models.CharField(max_length=500)
    unique_id = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    related = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    url = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.headline}'
