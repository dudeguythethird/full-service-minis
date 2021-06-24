from django.shortcuts import render
from .models import Product


def services(request):
    """A view to show the services explanation page."""

    return render(request, 'services/services.html')


def products(request):
    """A view to show all stocked products, as well as sorting them."""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'services/products.html', context) 