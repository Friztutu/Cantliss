
from django.urls import path

from django.contrib.auth.decorators import login_required
from basket.views import basket_add, basket_remove, BasketView

app_name = 'basket'

urlpatterns = [
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('basket/<int:user_id>/', login_required(BasketView.as_view()), name='basket')
]
