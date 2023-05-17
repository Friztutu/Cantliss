from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory

# Create your tests here.

class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Главная')
        self.assertTemplateUsed('products/index.html')


class CatalogViewTestCase(TestCase):
    fixtures = ('categories.json', 'products.json')

    def setUp(self):
        self.products = Product.objects.all()

    def _common_test(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Каталог')
        self.assertTemplateUsed('products/catalog.html')

    def test_view(self):
        path = reverse('catalog:catalog')
        response = self.client.get(path)

        self._common_test(response)
        self.assertEqual(list(response.context_data['object_list'][:3]), list(self.products)[:3])

    def test_view_with_category(self):
        category = ProductCategory.objects.first()

        path = reverse('catalog:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_test(response)

        self.assertEqual(
            list(response.context_data['object_list'][:3]),
            list(self.products.filter(category_id=category.id))[:3]
        )

    def test_view_with_page(self):
        path = reverse('catalog:catalog') + '?page=2'
        response = self.client.get(path)

        self._common_test(response)

        self.assertEqual(list(response.context_data['object_list']), list(self.products)[3:6])

    def test_view_with_page_and_category(self):
        category = ProductCategory.objects.get(id=2)
        path = reverse('catalog:category', kwargs={'category_id': category.id}) + '?page=2'
        response = self.client.get(path)

        self._common_test(response)

        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=category.id))[3:6]
        )
