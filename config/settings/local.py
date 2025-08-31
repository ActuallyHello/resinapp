import os
from config.settings.base import *
from dotenv import load_dotenv


load_dotenv()  # Загружает переменные из .env

# Debug-режим и доступные хосты
DEBUG = os.environ.get('APP_DEBUG', False)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Секретный ключ (только для разработки!)
SECRET_KEY = os.environ.get('APP_DJANGO_SECRET_KEY')

# База данных

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Настройки статических файлов
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Для разработки

# Media-файлы
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'apps.resincore': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'apps.resinauth': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
