from django.db import models
from users.models import CustomUser
from products.models import Product


# Create your models here.

class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен')
    )

    user = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT)
    basket_history = models.JSONField(default=dict)
    create_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField(default=CREATED, choices=STATUSES)
    email = models.EmailField()
