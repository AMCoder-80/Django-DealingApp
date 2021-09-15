from django.contrib import admin
from .models import *

# Register your models here.


@admin.action(description='تعیین مشاور')
def changer(model_admin, request, queryset):
    queryset.update(dealer=3)


class UserAdmin(admin.ModelAdmin):
    actions = [changer, ]


admin.site.register(User, UserAdmin)
admin.site.register(Dealer)