from django.urls import path
from .views import greeting

app_name = 'property'

urlpatterns = [
    path('', greeting, name='greeting')
]