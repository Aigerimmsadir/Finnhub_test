from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TicketInterest(models.Model):
    name = models.CharField(max_length=4,unique=True)
    users_subscribed = models.ManyToManyField(User,null=True,related_name='tickets')
