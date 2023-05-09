from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from common.views import TitleMixin
from orders.forms import OrderCreationForm
from django.urls import reverse_lazy
from orders.models import Order


# Create your views here.

class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    title = 'Создание заказа'
    form_class = OrderCreationForm
    success_url = reverse_lazy('orders:success')
    model = Order


class OrderView(TitleMixin, TemplateView):
    template_name = 'orders/order.html'
    title = 'Заказ'


class OrderListView(TitleMixin, TemplateView):
    template_name = 'orders/orders-list.html'
    title = 'Список заказов'


class OrderSuccessView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Успех'
