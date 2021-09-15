from django.db import models
from django.utils.html import format_html
from account.models import User, Dealer
from .utils import j_to_g


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
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='registered_properties', null=True)
    sale_type = models.CharField(max_length=1, choices=SALE_STATUS, verbose_name='نوع واگذاری')
    property_type = models.CharField(max_length=1, choices=PROPERTY_STATUS, verbose_name='نوع ملک')
    floor = models.SmallIntegerField(default=0, verbose_name='طبقه')
    location = models.TextField(verbose_name='آدرس')
    total_area = models.PositiveSmallIntegerField(verbose_name='متراژ کل')
    building_area = models.PositiveSmallIntegerField(verbose_name='متراژ زیربنا')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'status': 'O', },
                              related_name='properties', verbose_name='مالک')
    # image = models.ImageField(verbose_name='تصاویر')
    created = models.DateTimeField(auto_now_add=True)
    date_built = models.DateField(verbose_name='تاریخ ساخت')
    price = models.PositiveBigIntegerField(verbose_name='قیمت')
    options = models.ManyToManyField(Options, verbose_name='امکانات', blank=True)
    requesters = models.ManyToManyField(User, limit_choices_to={'status': 'B'},
                                        related_name='requested_properties', blank=True, verbose_name='متقاضیان')

    @property
    def get_full_intro(self):
        status = {
            'A': 'آپارتمان',
            'S': 'فروش',
            'R': 'اجاره',
            'H': 'ویلایی'
        }
        return status[self.property_type] + " " + str(self.total_area) + " متری " + status[self.sale_type]

    @property
    def get_property_status(self):
        status = {
            'A': 'آپارتمان',
            'H': 'ویلایی'
        }
        return status[self.property_type]

    @property
    def get_sale_type(self):
        status = {
            'S': 'فروش',
            'R': 'اجاره',
        }
        return status[self.sale_type]

    def image_tag(self):
        try:
            image = format_html(
                f"<img class='title-img' src='{self.images.all()[0].image.url}' width='115' height='100' "
                f"style='border-radius: 15px'>")
        except:
            image = format_html(
                f"<img class='title-img' src='/media/no_image.jpg' width='115' height='100' "
                f"style='border-radius: 15px'>")
        return image

    image_tag.short_description = 'تصویر اصلی'

    @property
    def get_property_options(self):
        return format_html('<br>'.join([i.name for i in self.options.all()]))

    def jalali_date(self):
        print(j_to_g(self.date_built))
        return j_to_g(self.date_built)

    def __str__(self):
        return self.get_full_intro

    class Meta:
        verbose_name = 'ملک'
        verbose_name_plural = 'املاک'


class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(default='no_image.jpg', verbose_name='تصویر')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
