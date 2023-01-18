"""
profアプリケーションのモデル定義ファイル

1. Profileモデル
2. Skillsモデル
3. CareersListモデル
4. Studyモデル
5. Commentsモデル
"""
from django.db import models


class Profile(models.Model):
    """Profileモデルを定義"""
    home_address = models.CharField(max_length=20)
    careers_text = models.TextField()
    hobbies = models.TextField()

    def __str__(self):
        """
        管理画面のレコードを判別するためのタイトルを定義する

        Returns
        -------
        record_title: str
            管理画面のレコードを判別するためのタイトル
        """
        return 'jin'


class Skills(models.Model):
    """Skillsモデルを定義"""
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='skills')
    skill = models.CharField(max_length=20)


class CareersList(models.Model):
    """CareersListモデルを定義"""
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='careers_list')
    company = models.CharField(max_length=20)
    job = models.CharField(max_length=20)


class Study(models.Model):
    """Studyモデルを定義"""
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        """
        管理画面のレコードを判別するためのタイトルを定義する

        Returns
        -------
        record_title: str
            管理画面のレコードを判別するためのタイトル
        """
        return self.title


class Comments(models.Model):
    """Commentsモデルを定義"""
    study = models.ForeignKey(
        Study,
        on_delete=models.CASCADE,
        related_name='comments')
    comment = models.TextField()
    created_at = models.DateField()
