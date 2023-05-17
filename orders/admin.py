from django.contrib import admin

from orders.models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_at', 'status', 'email')
    fields = (
        'id',
        ('first_name', 'last_name'),
        ('email', 'address'),
        ('status', 'create_at'),
        'basket_history',

    )
    readonly_fields = ('create_at', 'id')
