import django_filters
from django_filters import CharFilter, NumberFilter

from .models import Property


class MyFilter(django_filters.FilterSet):
    location = CharFilter(field_name='location', lookup_expr='icontains')
    price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Property
        fields = ['sale_type', 'property_type', 'location']
