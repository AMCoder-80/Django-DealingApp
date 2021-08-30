from django.urls import path
from .views import greeting, Home, PropertyCreation

app_name = 'property'

urlpatterns = [
    path('', greeting, name='greeting'),
    path('properties/', Home.as_view(), name='home'),
    path('property-creation/', PropertyCreation.as_view(), name='property_creation'),
]