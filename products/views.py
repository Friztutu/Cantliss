from django.shortcuts import render
from products.models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'products/index.html', context=context)


def catalog(request, category_id=None):
    if category_id:
        category: object = ProductCategory.objects.get(id=category_id)
        products: object = Product.objects.filter(category=category)
    else:
        products: object = Product.objects.all()
    context = {
        'title': 'Каталог',
        'products': products,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/catalog.html', context=context)
