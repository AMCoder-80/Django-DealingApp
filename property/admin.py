from django.contrib import admin

from .models import Property, Options, PropertyImages


# Register your models here.


@admin.action(description='تعیین مشاور')
def changer(model_admin, request, queryset):
    queryset.update(dealer=3)


class PropertyAdmin(admin.ModelAdmin):
    actions = [changer, ]


admin.site.register(Property, PropertyAdmin)
admin.site.register(Options)
admin.site.register(PropertyImages)
