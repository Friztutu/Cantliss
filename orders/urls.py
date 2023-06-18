from django.contrib.auth.decorators import login_required
from django.urls import path

from orders.views import (OrderCanceledView, OrderCreateView, OrderListView,
                          OrderSuccessView, OrderView, OrderAdminListView)

app_name = 'orders'

urlpatterns = [
    path('create/', login_required(OrderCreateView.as_view()), name='order_create'),
    path('<int:pk>/', login_required(OrderView.as_view()), name='order'),
    path('list/', login_required(OrderListView.as_view()), name='order_list'),
    path('success/<int:order_id>/', OrderSuccessView.as_view(), name='order_success'),
    path('canceled/', OrderCanceledView.as_view(), name='canceled'),
    path('order-admin-list/', login_required(OrderAdminListView.as_view()), name='order_admin_list'),
]
