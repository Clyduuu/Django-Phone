from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Manufacturer, Phone, Accessory

class AnotherView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("This is another view.")

def home(request):
    return render(request, 'home.html')

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer_list.html', {'manufacturers': manufacturers})

def manufacturer_detail(request, manufacturer_id):
    manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
    phones = Phone.objects.filter(manufacturer=manufacturer)
    return render(request, 'manufacturer_detail.html', {'manufacturer': manufacturer, 'phones': phones})

def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone_list.html', {'phones': phones})

def phone_detail(request, phone_id):
    phone = get_object_or_404(Phone, pk=phone_id)
    accessories = Accessory.objects.filter(phone=phone)
    return render(request, 'phone_detail.html', {'phone': phone, 'accessories': accessories})

def accessory_list(request):
    accessories = Accessory.objects.all()
    return render(request, 'accessory_list.html', {'accessories': accessories})

def accessory_detail(request, accessory_id):
    accessory = get_object_or_404(Accessory, pk=accessory_id)
    return render(request, 'accessory_detail.html', {'accessory': accessory})
