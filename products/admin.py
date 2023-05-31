from django.contrib import admin

from products.models import Product, ProductCategory, ProductGender

# Register your models here.


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'slug')
    fields = ('name', 'description',  ('price', 'quantity'), ('category', 'gender'), 'img', 'slug')
    search_fields = ('name', )
    ordering = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fields = ('name', 'slug')
    search_fields = ('name',)
    ordering = ('name', )
    prepopulated_fields = {'slug': ('name', )}


@admin.register(ProductGender)
class AdminProductGender(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fields = ('name', 'slug')
    search_fields = ('name', )
    ordering = ('name', )
    prepopulated_fields = {'slug': ('name', )}
