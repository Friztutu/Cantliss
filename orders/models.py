from django.db import models
from users.models import CustomUser
from products.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT)
    products = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    is_paid = models.BooleanField(default=False)
