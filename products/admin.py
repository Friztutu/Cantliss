from django.contrib import admin
from products.models import ProductCategory, Product

# Register your models here.


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description',  ('price', 'quantity'), 'category', 'img')
    readonly_fields = ('quantity',)
    search_fields = ('name', )
    ordering = ('name', )


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name', )
