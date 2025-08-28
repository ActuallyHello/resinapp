import os
from config.settings.base import *
from dotenv import load_dotenv

load_dotenv()  # Загружает переменные из .env

# Безопасность
DEBUG = os.environ.get('APP_DEBUG', False)
ALLOWED_HOSTS = ['...', '...']


# Секретный ключ (должен браться из переменных окружения!)
SECRET_KEY = os.environ.get('APP_DJANGO_SECRET_KEY')

# PostgreSQL
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

# Статика и медиа (на продакшене обычно через Nginx)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Для collectstatic
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# HTTPS-настройки
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
