from django.contrib import admin

from products.models import Product, ProductCategory, ProductGender, TypeProduct

# Register your models here.


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'type', 'slug')
    fields = ('name', 'description',  ('price', 'quantity'), ('gender', 'category', 'type'), 'img', 'slug')
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


@admin.register(TypeProduct)
class AdminProductType(admin.ModelAdmin):
    list_display = ('name', 'category')
    fields = ('name', 'category', 'slug', 'gender')
    search_fields = ('name', )
    ordering = ('name', )
    prepopulated_fields = {'slug': ('name',)}
