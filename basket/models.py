from django.db import models
from products.models import Product
from users.models import CustomUser


# Create your models here.

class Basket(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} || {self.product.name}'

    def get_total_sum(self):
        return self.product.price * self.quantity
