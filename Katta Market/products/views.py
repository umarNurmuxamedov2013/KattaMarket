from django.shortcuts import render
from .models import Product


def product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)
