from django.contrib import admin

from products.models import Product, ProductCategory

# Register your models here.


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'slug')
    fields = ('name', 'description',  ('price', 'quantity'), 'category', 'img', 'slug')
    search_fields = ('name', )
    ordering = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fields = ('name', 'description', 'slug')
    search_fields = ('name',)
    ordering = ('name', )
    prepopulated_fields = {'slug': ('name', )}
