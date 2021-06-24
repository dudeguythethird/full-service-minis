from django.contrib import admin
from .models import Product, Category, PaintTier


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'base_price',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class PaintTierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price_multiplier'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PaintTier, PaintTierAdmin)
