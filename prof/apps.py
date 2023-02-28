"""アプリケーション設定ファイル"""
from django.apps import AppConfig


class ProfConfig(AppConfig):
    """profアプリケーション構成を設定"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "prof"
