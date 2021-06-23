from django.contrib import admin
from .models import Product, Category, PaintTier


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(PaintTier)
