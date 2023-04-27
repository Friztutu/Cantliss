from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory
from basket.models import Basket
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
