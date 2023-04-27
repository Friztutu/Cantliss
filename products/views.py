from django.shortcuts import render
from products.models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'products/index.html', context=context)


def catalog(request, category_id=None):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    context = {
        'title': 'Каталог',
        'products': products,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/catalog.html', context=context)
