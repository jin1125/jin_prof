from django.shortcuts import render
from django.test import RequestFactory
from django.test import TestCase


class ErrorPagesTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_403_response(self):
        request = self.factory.get('/test/')
        response = render(request, '403.html', status=403)
        self.assertEqual(response.status_code, 403)
        self.assertIn('Forbidden (403)', response.content.decode())

    def test_404_response(self):
        request = self.factory.get('/test/')
        response = render(request, '404.html', status=404)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Page not found (404)', response.content.decode())

    def test_500_response(self):
        request = self.factory.get('/test/')
        response = render(request, '500.html', status=500)
        self.assertEqual(response.status_code, 500)
        self.assertIn('Server Error (500)', response.content.decode())
