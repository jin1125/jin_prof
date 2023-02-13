"""
profアプリケーションのテストコードファイル

1. Index
2. Study
"""
import datetime

from django.test import TestCase
from django.urls import resolve
from django.urls import reverse

from prof.models import CareersList
from prof.models import Comments
from prof.models import Profile
from prof.models import Skills
from prof.models import Study
from prof.views import IndexView
from prof.views import StudyView


class IndexPageTest(TestCase):
    """Indexのテスト"""
    def setUp(self):
        """"テストの初期設定"""
        self.profile = Profile.objects.create(
            home_address='home_address',
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

    def test_get_return_200(self):
        """ステータスコード200のレスポンスが返ってくるかテスト"""
        response = self.client.get(reverse('prof:index'))
        self.assertEqual(response.status_code, 200)

    def test_uses_expected_view(self):
        """URLパスとビューがマッピングされているかテスト"""
        view = resolve(reverse('prof:index'))
        self.assertEqual(view.func.view_class, IndexView)

    def test_uses_expected_template(self):
        """想定したテンプレートのレスポンスが返ってくるかテスト"""
        response = self.client.get(reverse('prof:index'))
        self.assertTemplateUsed(response, 'prof/index.html')

    def test_should_return_profile_home_address(self):
        """DBの「home_address」が表示されるかテスト"""
        response = self.client.get(reverse('prof:index'))
        self.assertContains(response, self.profile.home_address)

    def test_should_return_profile_careers_text(self):
        """DBの「careers_text」が表示されるかテスト"""
        response = self.client.get(reverse('prof:index'))
        self.assertContains(response, self.profile.careers_text)

    def test_should_return_profile_hobbies(self):
        """DBの「hobbies」が表示されるかテスト"""
        response = self.client.get(reverse('prof:index'))
        self.assertContains(response, self.profile.hobbies)

    def test_should_return_profile_skills_skill(self):
        """DBの「skill」が表示されるかテスト"""
        response = self.client.get(reverse('prof:index'))
        self.assertContains(response, self.skills.skill)

    def test_should_return_profile_careers_list_company(self):
        """DBの「company」が表示されるかテスト"""
        response = self.client.get(reverse('prof:index'))
        self.assertContains(response, self.careers_list.company)

    def test_should_return_profile_careers_list_job(self):
        """DBの「job」が表示されるかテスト"""
        response = self.client.get(reverse('prof:index'))
        self.assertContains(response, self.careers_list.job)


class StudyPageTest(TestCase):
    """Studyのテスト"""
    def setUp(self):
        """"テストの初期設定"""
        self.study = Study.objects.create(
            title='title',
            url='https://github.com/',
        )
        self.comments = Comments.objects.create(
            study=self.study,
            comment='comment',
            created_at=datetime.date.today(),
        )

    def test_get_return_200(self):
        """ステータスコード200のレスポンスが返ってくるかテスト"""
        response = self.client.get(reverse('prof:study'))
        self.assertEqual(response.status_code, 200)

    def test_uses_expected_view(self):
        """URLパスとビューがマッピングされているかテスト"""
        view = resolve(reverse('prof:study'))
        self.assertEqual(view.func.view_class, StudyView)

    def test_uses_expected_template(self):
        """想定したテンプレートのレスポンスが返ってくるかテスト"""
        response = self.client.get(reverse('prof:study'))
        self.assertTemplateUsed(response, 'prof/study.html')

    def test_should_return_study_title(self):
        """DBの「title」が表示されるかテスト"""
        response = self.client.get(reverse('prof:study'))
        self.assertContains(response, self.study.title)

    def test_should_return_study_url(self):
        """DBの「url」が表示されるかテスト"""
        response = self.client.get(reverse('prof:study'))
        self.assertContains(response, self.study.url)

    def test_should_return_study_comments_comment(self):
        """DBの「comment」が表示されるかテスト"""
        response = self.client.get(reverse('prof:study'))
        self.assertContains(response, self.comments.comment)

    def test_should_return_study_comments_created_at(self):
        """DBの「created_at」が表示されるかテスト"""
        response = self.client.get(reverse('prof:study'))
        self.assertContains(
            response,
            self.comments.created_at.strftime('%Y/%m/%d'),
        )
