from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Dealer(AbstractUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class User(models.Model):
    STATUS = (
        ('O', 'Owner'),
        ('B', 'Buyer'),
    )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices=STATUS)
    is_special = models.BooleanField(default=False)
    identifier = models.CharField(max_length=30)
    min_budget = models.BigIntegerField()
    max_budget = models.BigIntegerField()

    def __str(self):
        return self.first_name + " " + self.last_name
