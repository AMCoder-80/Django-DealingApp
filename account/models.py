from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Dealer(AbstractUser):
    first_name = models.CharField(max_length=60, verbose_name='نام')
    last_name = models.CharField(max_length=60, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'مشاور'
        verbose_name_plural = 'مشاوران'


class User(models.Model):
    STATUS = (
        ('O', 'مالک'),
        ('B', 'خریدار'),
    )
    first_name = models.CharField(max_length=60, verbose_name='نام')
    last_name = models.CharField(max_length=60, verbose_name='نام خانوادگی')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='تلفن')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name='وضعیت')
    max_budget = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='حداکثر بودجه')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
