# base views
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

# models
from products.models import Product, ProductCategory


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Главная'
        return context


class CatalogView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogView, self).get_context_data()
        context['title'] = 'Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(CatalogView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        queryset = queryset.filter(category_id=category_id) if category_id else queryset
        return queryset
