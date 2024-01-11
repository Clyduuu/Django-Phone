# myapp/urls.py
from django.urls import path
from .views import (
    home,
    manufacturer_list,
    manufacturer_detail,
    phone_list,
    phone_detail,
    accessory_list,
    accessory_detail,
    airpods_list,
    airpods_detail,
    tv_list,
    tv_detail,
)

app_name = 'myapp'  # Set the app_name for namespacing

urlpatterns = [
    path('', home, name='home'),
    path('manufacturers/', manufacturer_list, name='manufacturer_list'),
    path('manufacturers/<int:manufacturer_id>/', manufacturer_detail, name='manufacturer_detail'),
    path('phones/', phone_list, name='phone_list'),
    path('phones/<int:phone_id>/', phone_detail, name='phone_detail'),
    path('accessories/', accessory_list, name='accessory_list'),
    path('accessories/<int:accessory_id>/', accessory_detail, name='accessory_detail'),
    path('airpods/', airpods_list, name='airpods_list'),
    path('airpods/<int:airpods_id>/', airpods_detail, name='airpods_detail'),
    path('tv/', tv_list, name='tv_list'),
    path('tv/<int:tv_id>/', tv_detail, name='tv_detail'),
]
