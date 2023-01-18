"""
profアプリケーションのテストコードファイル

1. IndexViewに対するテスト
2. IndexViewに対するテスト(Profileモデルのレンダリング)
3. StudyViewに対するテスト
4. StudyViewに対するテスト(Studyモデルのレンダリング)
"""
import datetime
from django.test import TestCase
from django.urls import resolve

from prof.models import CareersList
from prof.models import Comments
from prof.models import Profile
from prof.models import Skills
from prof.models import Study
from prof.views import IndexView
from prof.views import StudyView


class IndexPageTest(TestCase):
    """IndexViewに対するテスト"""
    def test_index_page_returns_200(self):
        """
        /にGETリクエストを行い、
        ステータス200のレスポンスが返ってくるかテスト
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_uses_expected_view(self):
        """/にIndexViewが関連付いているかテスト"""
        view = resolve('/')
        self.assertEqual(view.func.view_class, IndexView)

    def test_index_page_uses_expected_template(self):
        """
        /にGETリクエストを行い、
        prof/index.htmlテンプレートがレスポンスで返ってくるかテスト
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'prof/index.html')


class IndexPageRenderProfileTest(TestCase):
    """IndexViewに対するテスト(Profileモデルのレンダリング)"""
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

    def test_should_return_profile_home_address(self):
        """
        /にGETリクエストを行い、
        home_addressの値がページに表示されるかテスト
        """
        response = self.client.get('/')
        self.assertContains(response, self.profile.home_address)

    def test_should_return_profile_careers_text(self):
        """
        /にGETリクエストを行い、
        careers_textの値がページに表示されるかテスト
        """
        response = self.client.get('/')
        self.assertContains(response, self.profile.careers_text)

    def test_should_return_profile_hobbies(self):
        """
        /にGETリクエストを行い、
        hobbiesの値がページに表示されるかテスト
        """
        response = self.client.get('/')
        self.assertContains(response, self.profile.hobbies)

    def test_should_return_profile_skills_skill(self):
        """
        /にGETリクエストを行い、
        skillの値がページに表示されるかテスト
        """
        response = self.client.get('/')
        self.assertContains(response, self.skills.skill)

    def test_should_return_profile_careers_list_company(self):
        """
        /にGETリクエストを行い、
        companyの値がページに表示されるかテスト
        """
        response = self.client.get('/')
        self.assertContains(response, self.careers_list.company)

    def test_should_return_profile_careers_list_job(self):
        """
        /にGETリクエストを行い、
        jobの値がページに表示されるかテスト
        """
        response = self.client.get('/')
        self.assertContains(response, self.careers_list.job)


class StudyPageTest(TestCase):
    """StudyViewに対するテスト"""
    def test_study_page_returns_200(self):
        """
        /study/にGETリクエストを行い、
        ステータス200のレスポンスが返ってくるかテスト
        """
        response = self.client.get('/study/')
        self.assertEqual(response.status_code, 200)

    def test_study_page_uses_expected_view(self):
        """/study/にStudyViewが関連付いているかテスト"""
        view = resolve('/study/')
        self.assertEqual(view.func.view_class, StudyView)

    def test_study_page_uses_expected_template(self):
        """
        /study/にGETリクエストを行い、
        prof/study.htmlテンプレートがレスポンスで返ってくるかテスト
        """
        response = self.client.get('/study/')
        self.assertTemplateUsed(response, 'prof/study.html')


class StudyPageRenderStudyTest(TestCase):
    """StudyViewに対するテスト(Studyモデルのレンダリング)"""
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

    def test_should_return_study_title(self):
        """
        /study/にGETリクエストを行い、
        titleの値がページに表示されるかテスト
        """
        response = self.client.get('/study/')
        self.assertContains(response, self.study.title)

    def test_should_return_study_url(self):
        """
        /study/にGETリクエストを行い、
        urlの値がページに表示されるかテスト
        """
        response = self.client.get('/study/')
        self.assertContains(response, self.study.url)

    def test_should_return_study_comments_comment(self):
        """
        /study/にGETリクエストを行い、
        commentの値がページに表示されるかテスト
        """
        response = self.client.get('/study/')
        self.assertContains(response, self.comments.comment)

    def test_should_return_study_comments_created_at(self):
        """
        /study/にGETリクエストを行い、
        created_atの値がページに表示されるかテスト
        """
        response = self.client.get('/study/')
        self.assertContains(
            response,
            self.comments.created_at.strftime('%Y/%m/%d')
        )
