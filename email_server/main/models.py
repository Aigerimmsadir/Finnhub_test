from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser

# src/users/model.py
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        return self.create_user(email, password, **extra_fields)




class MainUser(AbstractUser):
    username = None
    email = models.EmailField( unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
class TicketInterest(models.Model):
    name = models.CharField(max_length=4, unique=True)
    users_subscribed = models.ManyToManyField(
        'MainUser', null=True, related_name='tickets')


class CompanyNew(models.Model):
    id = models.AutoField(primary_key=True)
    datetime_created = models.DateTimeField()
    headline = models.CharField(max_length=500)
    unique_id = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    related = models.ForeignKey(TicketInterest,null=True,on_delete=models.CASCADE)
    source = models.CharField(max_length=500)
    summary = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f'{self.headline}'
