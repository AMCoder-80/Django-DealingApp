from django.db import models

from account.models import User


# Create your models here.


class Options(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی'

class Property(models.Model):
    SALE_STATUS = (
        ('R', 'اجاره'),
        ('S', 'فروش'),
    )
    PROPERTY_STATUS = (
        ('A', 'آپارتمان'),
        ('H', 'ویلایی'),
    )
    sale_type = models.CharField(max_length=1, choices=SALE_STATUS, verbose_name='نوع واگذاری')
    property_type = models.CharField(max_length=1, choices=PROPERTY_STATUS, verbose_name='نوع ملک')
    floor = models.SmallIntegerField(default=0, verbose_name='طبقه')
    location = models.TextField(verbose_name='آدرس')
    total_area = models.PositiveSmallIntegerField(verbose_name='متراژ کل')
    building_area = models.PositiveSmallIntegerField(verbose_name='متراژ زیربنا')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'status': 'O'},
                              related_name='properties', verbose_name='مالک')
    image = models.ImageField(verbose_name='تصاویر')
    created = models.DateTimeField(auto_now_add=True)
    date_built = models.DateField(verbose_name='تاریخ ساخت')
    price = models.PositiveBigIntegerField(verbose_name='قیمت')
    options = models.ManyToManyField(Options, verbose_name='امکانات')
    requesters = models.ManyToManyField(User, limit_choices_to={'status': 'B'},
                 related_name='requested_properties', null=True, blank=True, verbose_name='متقاضیان')

    def __str__(self):
        status = {
            'A': 'آپارتمان',
            'S': 'فروش',
            'R': 'اجاره',
            'H': 'ویلایی'
        }
        return status[self.property_type] + " " + str(self.total_area) + " متری " + status[self.sale_type]

    class Meta:
        verbose_name = 'ملک'
        verbose_name_plural = 'املاک'
