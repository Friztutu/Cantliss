
from django.urls import path

from products.views import CardView, CatalogView, IndexView, add_favorite, remove_favorite

app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/<slug:gender_slug>/', CatalogView.as_view(), name='catalog'),
    path('catalog/<slug:gender_slug>/<slug:category_slug>/', CatalogView.as_view(), name='category'),
    path('catalog/card/<slug:gender_slug>/<slug:product_slug>', CardView.as_view(), name='card'),
    path('favorite/add/<int:product_id>', add_favorite, name='add_favorite'),
    path('favorite/remove/<int:favorite_id>', remove_favorite, name='remove_favorite'),
]
