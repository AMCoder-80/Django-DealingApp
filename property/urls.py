from django.urls import path
from .views import greeting, Home

app_name = 'property'

urlpatterns = [
    path('', greeting, name='greeting'),
    path('properties/', Home.as_view(), name='home')
]