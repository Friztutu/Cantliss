from django.urls import path
from products.views import index, catalog


app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('catalog', catalog, name='catalog'),
]
