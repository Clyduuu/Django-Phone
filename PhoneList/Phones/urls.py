# Phones/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('manufacturer_list/', views.manufacturer_list, name='manufacturer_list'),
    path('manufacturer_detail/<int:manufacturer_id>/', views.manufacturer_detail, name='manufacturer_detail'),
    path('phone_list/', views.phone_list, name='phone_list'),
    path('phone_detail/<int:phone_id>/', views.phone_detail, name='phone_detail'),
    path('accessory_list/', views.accessory_list, name='accessory_list'),
    path('accessory_detail/<int:accessory_id>/', views.accessory_detail, name='accessory_detail'),
    # Add more URL patterns as needed
]
