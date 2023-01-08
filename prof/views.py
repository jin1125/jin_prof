from django.views.generic import ListView
from .models import Profile


class IndexView(ListView):
    model = Profile
    template_name = 'prof/index.html'
