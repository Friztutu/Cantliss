from django.db import models
from products.models import Product
from users.models import CustomUser


# Create your models here.


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
        return f'{self.user.name} || {self.product.name}'

    def get_product_sum(self):
        return self.product.price * self.quantity
