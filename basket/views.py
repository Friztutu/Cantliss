from django.shortcuts import render
from products.models import Product, ProductCategory
from basket.models import Basket

# Create your views here.

def basket_add(request, product_id):
    pass