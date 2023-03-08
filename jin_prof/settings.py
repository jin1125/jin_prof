"""
Djangoの設定ファイル

- 環境変数設定
- カスタム設定
- Django設定
- アプリケーション設定
- ミドルウェア設定
- Staticファイル設定
"""
from pathlib import Path

import environ


# 環境変数設定
env = environ.Env()
env.read_env('.env')

ADMIN_PATH = env('ADMIN_PATH', default='admin') + '/'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

DEBUG = env.bool('DEBUG', default=True)

DATABASES = {
    'default': env.db(),
    'TEST': {
        'MIRROR': 'default',
    },
}

SECRET_KEY = env('SECRET_KEY')

# カスタム設定
GOOGLE_ANALYTICS_TRACKING_ID = 'G-GSJGR2540P'

# Django設定
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]

BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROOT_URLCONF = 'jin_prof.urls'

LANGUAGE_CODE = 'ja'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'base': {
            'format': '[%(levelname)s] %(asctime)s '
            '%(pathname)s:%(lineno)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'base',
            'filters': ['require_debug_true'],
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'base',
            'filename': '/var/log/jin_prof/app.log',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'jin_prof.context_processors.get_ga_tracking_id',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

WSGI_APPLICATION = 'jin_prof.wsgi.application'

# アプリケーション設定
INSTALLED_APPS = [
    'prof.apps.ProfConfig',
    'fontawesomefree',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ミドルウェア設定
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Staticファイル設定
STATIC_URL = 'static/'

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / 'static']
else:
    STATIC_ROOT = BASE_DIR / 'static'
