from django.shortcuts import render
from products.models import Product, ProductCategory
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'products/index.html', context=context)


def catalog(request, category_id=None, page=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(object_list=products, per_page=3)
    products_paginator = paginator.page(page)

    context = {
        'title': 'Каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/catalog.html', context=context)
