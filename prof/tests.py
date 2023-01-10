from django.test import TestCase
from django.urls import resolve

from prof.models import CareersList
from prof.models import Profile
from prof.models import Skills
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


class IndexPageRenderProfileTest(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            careers_text='careers_text',
            hobbies='hobbies',
        )
        self.skills = Skills.objects.create(
            profile=self.profile,
            skill='careers_text',
        )
        self.careers_list = CareersList.objects.create(
            profile=self.profile,
            company='company',
            job='job',
        )

    def test_should_return_profile_careers_text(self):
        response = self.client.get('/')
        self.assertContains(response, self.profile.careers_text)

    def test_should_return_profile_hobbies(self):
        response = self.client.get('/')
        self.assertContains(response, self.profile.hobbies)

    def test_should_return_profile_skills_skill(self):
        response = self.client.get('/')
        self.assertContains(response, self.skills.skill)

    def test_should_return_profile_careers_list_company(self):
        response = self.client.get('/')
        self.assertContains(response, self.careers_list.company)

    def test_should_return_profile_careers_list_job(self):
        response = self.client.get('/')
        self.assertContains(response, self.careers_list.job)


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
