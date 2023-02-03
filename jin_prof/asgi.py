"""ASGIアプリケーションの設定ファイル"""
import os

from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jin_prof.settings')

application = get_asgi_application()
