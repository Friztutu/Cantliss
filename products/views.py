from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Product, ProductCategory, ProductGender, FavoriteProduct
from django.contrib.auth.decorators import login_required


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

        if category_slug == 'not-available':
            queryset = queryset.filter(quantity=0, gender__slug=gender_slug)
        else:
            queryset = queryset.filter(category__slug=category_slug,
                                       gender__slug=gender_slug) if category_slug else queryset.filter(
                gender__slug=gender_slug)

        return queryset


class CardView(TitleMixin, TemplateView):
    template_name = 'products/card.html'
    title = 'Карточка товара'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = ProductCategory.objects.all()
        context['product'] = Product.objects.get(slug=self.kwargs.get('product_slug'))
        context['is_favorite'] = True if FavoriteProduct.objects.filter(product__slug=self.kwargs.get('product_slug'), user=self.request.user) else False
        return context


@login_required
def add_favorite(request, product_id):
    product = Product.objects.get(id=product_id)
    FavoriteProduct.objects.create(user=request.user, product=product)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_favorite(request, favorite_id):
    favorite = FavoriteProduct.objects.get(id=favorite_id)
    if favorite:
        favorite.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
