from django.urls import path
from orders.views import OrderCreateView, OrderView, OrderListView, OrderSuccessView


app_name = 'orders'

urlpatterns = [
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order/', OrderView.as_view(), name='order'),
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('order_success/', OrderSuccessView.as_view(), name='order_success'),
]
