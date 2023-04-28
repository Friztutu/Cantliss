from django.contrib import admin
from users.models import CustomUser
from basket.admin import BasketAdmin


# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'is_superuser', 'is_staff')
    fields = (
        'username', ('first_name', 'last_name'),
        'email', 'password', 'img',
        ('is_superuser', 'is_staff', 'is_active'),
        'date_joined', 'user_permissions', 'groups'
    )
    readonly_fields = ('username', 'password', 'date_joined')
    search_fields = ('username',)
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    inlines = (BasketAdmin, )
