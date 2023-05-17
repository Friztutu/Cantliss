import uuid
from http import HTTPStatus

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from yookassa import Payment

from basket.models import Basket
from common.views import TitleMixin
from orders.forms import OrderCreationForm
from orders.models import Order

# Create your views here.

class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    title = 'Создание заказа'
    form_class = OrderCreationForm
    success_url = reverse_lazy('orders:order_success', kwargs={'order_id': 1})
    model = Order

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OrderCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        idempotence_key = str(uuid.uuid4())
        user_basket = Basket.objects.filter(user=request.user)
        order_id = Order.objects.last().id
        payment = Payment.create({
            "amount": {
                "value": f"{user_basket.get_total_sum()}",
                "currency": "RUB"
            },
            "payment_method_data": {
                "type": "bank_card"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "{}{}".format(settings.DOMAIN_NAME,
                                            reverse('orders:order_success', kwargs={'order_id': order_id}))
            },
            "description": f"Заказ {order_id}"
        }, idempotence_key)

        return HttpResponseRedirect(payment.confirmation.confirmation_url, status=HTTPStatus.SEE_OTHER)


class OrderCanceledView(TitleMixin, TemplateView):
    template_name = 'orders/canceled.html'
    title = 'Ошибка'


class OrderView(TitleMixin, DetailView):
    template_name = 'orders/order.html'
    title = 'Заказ'
    model = Order


class OrderListView(TitleMixin, ListView):
    template_name = 'orders/orders-list.html'
    title = 'Список заказов'
    queryset = Order.objects.all()
    ordering = '-create_at'

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.user.id
        queryset = queryset.filter(user_id=user_id)
        return queryset


class OrderSuccessView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Успех'

    def get(self, request, *args, **kwargs):
        order = Order.objects.get(id=self.kwargs.get('order_id'))
        order.update_after_payment()
        return super().get(request, *args, **kwargs)
