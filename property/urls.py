from django.urls import path
from .views import *

app_name = 'property'

urlpatterns = [
    path('', greeting, name='greeting'),
    path('properties/', Home.as_view(), name='home'),
    path('properties/add-requester/<int:pk>', UpdateRequesters.as_view(), name='add_requester'),
    path('property-creation/', PropertyCreation.as_view(), name='property_creation'),
    path('property-update/<int:pk>', PropertyUpdate.as_view(), name='property_update'),
    path('property-detail/<int:pk>', PropertyDetail.as_view(), name='detail_property'),
    path('property-delete/<int:pk>', PropertyDelete.as_view(), name='property_delete'),
]