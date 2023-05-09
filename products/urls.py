
from django.urls import path

from products.views import CatalogView, IndexView

app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/category/<slug:category_slug>', CatalogView.as_view(), name='category'),
]
