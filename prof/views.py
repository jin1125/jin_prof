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
    model = Profile
    template_name = 'prof/index.html'


class StudyView(ListView):
    template_name = 'prof/study.html'

    def get_queryset(self):
        return Study.objects.annotate(
            latest_created_at=Max('comments__created_at')
        ).order_by('-latest_created_at')
