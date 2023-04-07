from django.urls import path, include
from products.views import index, catalog

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
]
