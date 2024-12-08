from django.contrib import admin
from .models import Brand,Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','headquarters','established_year')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name','price','brand','year')

