from django.urls import path, include
from basket.views import basket_add

app_name = 'basket'

urlpatterns = [
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
]
