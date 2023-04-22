from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)
    img = models.ImageField(upload_to=r'product_img')

    def __str__(self):
        return self.name
