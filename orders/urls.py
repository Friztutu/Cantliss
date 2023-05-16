from django.urls import path
from orders.views import OrderCreateView, OrderView, OrderListView, OrderSuccessView, OrderCanceledView
from django.contrib.auth.decorators import login_required


app_name = 'orders'

urlpatterns = [
    path('order_create/', login_required(OrderCreateView.as_view()), name='order_create'),
    path('order/<int:pk>/', OrderView.as_view(), name='order'),
    path('order_list/<int:user_id>/', login_required(OrderListView.as_view()), name='order_list'),
    path('order_success/<int:order_id>/', OrderSuccessView.as_view(), name='order_success'),
    path('order_canceled', OrderCanceledView.as_view(), name='canceled')
]
