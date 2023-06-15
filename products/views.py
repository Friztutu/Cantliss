
from django.core.cache import cache
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Product, ProductCategory, ProductGender


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Главная'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['genders'] = ProductGender.objects.all()
        return context


class CatalogView(TitleMixin, ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 20
    title = 'Каталог'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogView, self).get_context_data()
        categories = cache.get('categories')
        if categories:
            context['categories'] = ProductCategory.objects.all()
            cache.set('categories', context['categories'], 30)
        else:
            context['categories'] = categories
        context['categories'] = ProductCategory.objects.all()
        context['category_slug'] = self.kwargs.get('category_slug')
        return context

    def get_queryset(self):
        queryset = super(CatalogView, self).get_queryset()
        category_slug = self.kwargs.get('category_slug')
        gender_slug = self.kwargs.get('gender_slug')
        queryset = queryset.filter(category__slug=category_slug, gender__slug=gender_slug) if category_slug else queryset.filter(gender__slug=gender_slug)
        return queryset


class CardView(TitleMixin, TemplateView):
    template_name = 'products/card.html'
    title = 'Карточка товара'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = ProductCategory.objects.all()
        context['product'] = Product.objects.get(slug=self.kwargs.get('product_slug'))
        return context
