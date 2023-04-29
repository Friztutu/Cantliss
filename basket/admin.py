# settings
from django.contrib import admin

# models
from basket.models import Basket


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_at')
    readonly_fields = ('created_at', 'product', 'quantity')
    extra = 0
