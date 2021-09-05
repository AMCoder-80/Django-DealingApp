from django.contrib import admin
from .models import Property, Options, PropertyImages

# Register your models here.

admin.site.register(Property)
admin.site.register(Options)
admin.site.register(PropertyImages)