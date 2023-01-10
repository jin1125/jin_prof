from django.test import TestCase
from django.urls import resolve

from prof.views import IndexView


class IndexPageTest(TestCase):
    def test_index_page_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_uses_expected_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, IndexView)

    def test_index_page_uses_expected_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'prof/index.html')
