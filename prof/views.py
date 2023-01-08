from django.views.generic import ListView

from .models import Profile
from .models import Study


class IndexView(ListView):
    model = Profile
    template_name = 'prof/index.html'


class StudyView(ListView):
    model = Study
    template_name = 'prof/study.html'
