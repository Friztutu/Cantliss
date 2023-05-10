from django.urls import path
from orders.views import OrderCreateView, OrderView, OrderListView, OrderSuccessView, OrderCanceledView
from django.contrib.auth.decorators import login_required


app_name = 'orders'

urlpatterns = [
    path('order_create/', login_required(OrderCreateView.as_view()), name='order_create'),
    path('order/', OrderView.as_view(), name='order'),
    path('order_list/', login_required(OrderListView.as_view()), name='order_list'),
    path('order_success/', OrderSuccessView.as_view(), name='order_success'),
    path('order_canceled', OrderCanceledView.as_view(), name='canceled')
]
