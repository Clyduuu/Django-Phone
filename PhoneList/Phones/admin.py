from django.contrib import admin
from .models import Manufacturer, Phone, Accessory, Airpods, TV

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price', 'release_date')
    list_filter = ('manufacturer', 'release_date')
    search_fields = ('name', 'manufacturer__name')

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'price')
    list_filter = ('phone__manufacturer', 'price')
    search_fields = ('name', 'phone__name')

# Register Airpods and TV models
@admin.register(Airpods)
class AirpodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price', 'release_date')
    list_filter = ('manufacturer', 'release_date')
    search_fields = ('name', 'manufacturer__name')

@admin.register(TV)
class TVAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price', 'release_date')
    list_filter = ('manufacturer', 'release_date')
    search_fields = ('name', 'manufacturer__name')
