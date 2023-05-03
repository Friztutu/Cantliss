from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Главная')
