from django import forms
from .models import OrderItem, Order, Customer, Category

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_date', 'total_amount', 'customer', 'products']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


