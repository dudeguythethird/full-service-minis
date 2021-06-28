from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('products/<product_id>', views.product_details, name='product_detail'),
]
