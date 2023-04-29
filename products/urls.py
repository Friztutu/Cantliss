# default import
from django.urls import path

# views
from products.views import IndexView, CatalogView


app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/category/int:<category_id>', CatalogView.as_view(), name='category'),
]
