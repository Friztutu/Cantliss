from django.shortcuts import render
from products.models import Product, ProductCategory
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'products/index.html'


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
