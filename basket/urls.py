# base import
from django.urls import path

# our controllers
from basket.views import basket_add, basket_remove

app_name = 'basket'

urlpatterns = [
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
