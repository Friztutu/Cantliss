import json

from django.db import models

from products.models import Product
from users.models import CustomUser


class BasketQuerySet(models.QuerySet):
    def get_total_sum(self):
        return sum(basket.get_product_sum() for basket in self)

    def get_total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'{self.product.name}'

    def get_product_sum(self):
        return self.product.price * self.quantity

    def get_json(self):
        basket_item = {
            'product_name': str(self.product.name),
            'quantity': int(self.quantity),
            'price': float(self.product.price),
            'sum': float(self.get_product_sum())
        }

        return basket_item
