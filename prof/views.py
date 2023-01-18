"""
profアプリケーションのビュー定義ファイル

1. IndexView
2. StudyView
"""
from django.db.models import Max
from django.views.generic import ListView

from prof.models import Profile
from prof.models import Study


class IndexView(ListView):
    """Profileモデルをリスト表示するビューを定義"""
    model = Profile
    template_name = 'prof/index.html'


class StudyView(ListView):
    """Studyモデルをリスト表示するビューを定義"""
    template_name = 'prof/study.html'

    def get_queryset(self):
        """
        参照しているCommentsモデルのコメント作成日が最新の順でStudyモデルを取得

        Returns
        -------
        study_model: django.db.models.query.QuerySet
            Studyモデル(参照しているCommentsモデルのコメント作成日の最新順)
        """
        return Study.objects.annotate(
            latest_created_at=Max('comments__created_at')
        ).order_by('-latest_created_at')
