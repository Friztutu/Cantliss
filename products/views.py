from django.shortcuts import render
from products.models import Product, Category


# Create your views here.

def index(request):
    return render(request, 'index.html')


def catalog(request):
    context = {'products': Product.objects.all(),
               'categories': Category.objects.all(),
               }
    return render(request, 'catalog.html', context=context)
