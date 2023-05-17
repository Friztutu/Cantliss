from django.urls import path
from orders.views import OrderCreateView, OrderView, OrderListView, OrderSuccessView, OrderCanceledView
from django.contrib.auth.decorators import login_required


app_name = 'orders'

urlpatterns = [
    path('create/', login_required(OrderCreateView.as_view()), name='order_create'),
    path('<int:pk>/', login_required(OrderView.as_view()), name='order'),
    path('list/', login_required(OrderListView.as_view()), name='order_list'),
    path('success/<int:order_id>/', OrderSuccessView.as_view(), name='order_success'),
    path('canceled', OrderCanceledView.as_view(), name='canceled')
]
