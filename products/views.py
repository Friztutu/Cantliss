# base views
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
# models
from products.models import Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Главная'


class CatalogView(TitleMixin, ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 3
    title = 'Каталог'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(CatalogView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        queryset = queryset.filter(category_id=category_id) if category_id else queryset
        return queryset
