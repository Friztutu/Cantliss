from django.shortcuts import render
from django.views.generic.base import TemplateView
from common.views import TitleMixin


# Create your views here.

class OrderCreateView(TitleMixin, TemplateView):
    template_name = 'orders/order-create.html'
    title = 'Создание заказа'


class OrderView(TitleMixin, TemplateView):
    template_name = 'orders/order.html'
    title = 'Заказ'


class OrderListView(TitleMixin, TemplateView):
    template_name = 'orders/orders-list.html'
    title = 'Список заказов'


class OrderSuccessView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Успех'
