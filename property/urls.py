from django.urls import path
from .views import *

app_name = 'property'

urlpatterns = [
    path('', greeting, name='greeting'),
    path('properties/', Home.as_view(), name='home'),
    path('property-creation/', PropertyCreation.as_view(), name='property_creation'),
    path('property-update/<int:pk>', PropertyUpdate.as_view(), name='property_update'),
    path('property-detail/<int:pk>', PropertyDetail.as_view(), name='detail_property'),
]