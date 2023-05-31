from django.db import models


# Create your models here.
class ProductGender(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'


class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)
    img = models.ImageField(upload_to=r'product_img')
    slug = models.SlugField(unique=True, verbose_name='URL')
    gender = models.ForeignKey(to=ProductGender, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
