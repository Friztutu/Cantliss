from django.urls import path, include
from products.views import catalog


app_name = 'products'


urlpatterns = [
    path('', catalog, name='catalog'),
]
