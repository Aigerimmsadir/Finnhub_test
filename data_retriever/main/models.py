from statistics import mode
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CompanyNew(models.Model):
    id = models.AutoField(primary_key=True)
    datetime_created = models.DateTimeField()
    headline = models.CharField(max_length=500)
    unique_id = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    related = models.CharField(max_length=500)
    source = models.CharField(max_length=500)
    summary = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f'{self.headline}'
