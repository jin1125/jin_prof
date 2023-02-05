"""
プロジェクトのURLマッピング定義ファイル

1. 管理サイトページ
2. profアプリケーションの各ページ
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path(settings.ADMIN_PATH, admin.site.urls),
    path('', include('prof.urls')),
]
