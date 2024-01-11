# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phones/', include('Phones.urls')),  # Use 'phones' here, not 'Phones'
]
