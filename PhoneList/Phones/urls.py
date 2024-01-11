from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CustomerListView,  
    CustomerDetailView, 
    CustomerCreateView, 
    CustomerUpdateView,  
    CustomerDeleteView,  
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    OrderItemListView, 
    OrderItemDetailView, 
    OrderItemCreateView, 
    OrderItemUpdateView, 
    OrderItemDeleteView,
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    path('customers/', CustomerListView.as_view(), name='customer-list'),  # Added CustomerListView
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),  # Added CustomerDetailView
    path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),  # Added CustomerCreateView
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),  # Added CustomerUpdateView
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),  # Added CustomerDeleteView

    path('orders/', OrderListView.as_view(), name='order-list'),  # Changed to OrderListView
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),  # Changed to OrderDetailView
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),  # Changed to OrderCreateView
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),  # Changed to OrderUpdateView
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),  # Changed to OrderDeleteView

    path('order_items/', OrderItemListView.as_view(), name='order-item-list'),  # Changed to OrderItemListView
    path('order_items/<int:pk>/', OrderItemDetailView.as_view(), name='order-item-detail'),  # Changed to OrderItemDetailView
    path('order_items/create/', OrderItemCreateView.as_view(), name='order-item-create'),  # Changed to OrderItemCreateView
    path('order_items/<int:pk>/update/', OrderItemUpdateView.as_view(), name='order-item-update'),  # Changed to OrderItemUpdateView
    path('order_items/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='order-item-delete'),  # Changed to OrderItemDeleteView

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

]
