from django.shortcuts import render
from products.models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'products/index.html', context=context)


def catalog(request):
    context = {
        'title': 'Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/catalog.html', context=context)
