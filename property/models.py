from django.db import models
from account.models import User

# Create your models here.


class Property(models.Model):
    SALE_STATUS = (
        ('R', 'Rent'),
        ('S', 'Sale'),
    )
    PROPERTY_STATUS = (
        ('A', 'Apartment'),
        ('H', 'House'),
    )
    sale_type = models.CharField(max_length=1, choices=SALE_STATUS)
    property_type = models.CharField(max_length=1, choices=PROPERTY_STATUS)
    floor = models.SmallIntegerField(default=0)
    location = models.TextField()
    total_area = models.PositiveSmallIntegerField()
    building_area = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    date_built = models.DateField()
    price = models.PositiveBigIntegerField()
    options = models.CharField(max_length=10)
    requesters = models.ManyToManyField(User, related_name='requested_properties')

    def __str__(self):
        return self.property_type + " " + str(self.total_area) + " " + self.sale_type
