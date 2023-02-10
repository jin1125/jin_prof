"""
profアプリケーションのビュー定義ファイル

1. indexページ
2. studyページ
"""
from django.db.models import Max
from django.views.generic import ListView

from prof.models import Profile
from prof.models import Study


class IndexView(ListView):
    """Profileモデルをリスト表示する処理を定義"""
    context_object_name = "profile_list"
    model = Profile
    template_name = 'prof/index.html'


class StudyView(ListView):
    """Studyモデルをリスト表示する処理を定義"""
    context_object_name = "study_list"
    queryset = Study.objects.annotate(
        latest_created_at=Max('comments__created_at'),
    ).order_by('-latest_created_at')
    template_name = 'prof/study.html'
