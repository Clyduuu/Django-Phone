from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product, Customer, Order, OrderItem, Category
from .forms import OrderItemForm, CategoryForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price', 'brand', 'category']

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price', 'brand', 'category']

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['first_name', 'last_name', 'email', 'phone']
    form_class = Customer

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['first_name', 'last_name', 'email', 'phone']
    form_class = Customer

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['customer', 'product', 'quantity', 'total_price']  

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['customer', 'product', 'quantity', 'total_price']
    form_class = Order  

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order-list')
    context_object_name = 'order'

class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'order_item_list.html'
    context_object_name = 'order_items'

class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'order_item_detail.html'
    context_object_name = 'order_item'

class OrderItemCreateView(CreateView):
    model = OrderItem
    template_name = 'order_item_form.html'
    success_url = reverse_lazy('order-item-list')
    form_class = OrderItemForm

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    template_name = 'order_item_form.html'
    success_url = reverse_lazy('order-item-list')
    form_class = OrderItemForm

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = 'order_item_confirm_delete.html'
    success_url = reverse_lazy('order-item-list')

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_form.html'
    form_class = CategoryForm

    def form_valid(self, form):
        return super().form_valid(form)

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_form.html'
    form_class = CategoryForm

    def form_valid(self, form):
        return super().form_valid(form)

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category-list')