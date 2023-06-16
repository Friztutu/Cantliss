from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.list import ListView
from basket.models import Basket
from products.models import Product


class BasketView(ListView):
    template_name = 'basket/basket.html'
    model = Basket

    def get(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.id
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(BasketView, self).get_queryset()
        user_id = self.kwargs.get('user_id')
        return queryset.filter(user_id=user_id)


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
