from django.test import TestCase
from django.urls import resolve

from prof.views import IndexView
from prof.views import StudyView


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


class StudyPageTest(TestCase):
    def test_study_page_returns_200(self):
        response = self.client.get('/study/')
        self.assertEqual(response.status_code, 200)

    def test_study_page_uses_expected_view(self):
        view = resolve('/study/')
        self.assertEqual(view.func.view_class, StudyView)

    def test_study_page_uses_expected_template(self):
        response = self.client.get('/study/')
        self.assertTemplateUsed(response, 'prof/study.html')
