# default import
from django.contrib import admin

# our models
from users.models import CustomUser, EmailVerification
from basket.admin import BasketAdmin


# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'is_superuser', 'is_staff')
    fields = (
        'username', ('first_name', 'last_name'),
        'email', 'password', 'img',
        ('is_superuser', 'is_staff', 'is_active'),
        'is_verified_email',
        'date_joined', 'user_permissions', 'groups'
    )
    readonly_fields = ('username', 'password', 'date_joined')
    search_fields = ('username',)
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'is_verified_email')
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'created_at', 'expiration')
    fields = ('code', 'user', 'created_at', 'expiration')
    readonly_fields = ('code', 'user', 'created_at', 'expiration')
    search_fields = ('user',)
