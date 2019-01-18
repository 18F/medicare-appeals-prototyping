from .base import *
from .env import env

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

DATABASES['default'] = dj_database_url.config(default=env.DATABASE_URL)

LOGGING = {}
