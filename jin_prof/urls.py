"""
URLマッピング定義ファイル

- 管理サイトページ
- profアプリケーションの各ページ
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path(settings.ADMIN_PATH, admin.site.urls),
    path('', include('prof.urls')),
]
