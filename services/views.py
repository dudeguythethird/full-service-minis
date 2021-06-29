from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def services(request):
    """A view to show the services explanation page."""

    return render(request, 'services/services.html')


def products(request):
    """A view to show all stocked products, as well as sorting them."""

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            categories = Category.objects.filter(name__in=category)

    context = {
        'products': products,
        'filter': categories,
    }

    return render(request, 'services/products.html', context)


def product_details(request, product_id):
    """A view to show an individual product's details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'services/product_detail.html', context)