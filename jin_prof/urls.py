from django.contrib import admin
from django.urls import path

from prof import views

app_name = 'prof'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]
