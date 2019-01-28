import dj_database_url
from .base import *
from .env import env

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

USE_X_FORWARDED_HOST = True

ALLOWED_HOSTS = ['*']  # proxied

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

STATIC_ROOT = '/app/medicare_appeals/static/'
STATIC_URL = '/static/'

rds = env.get_service(label='aws-rds')

DATABASES['default'] = dj_database_url.config(default=rds.credentials['uri'])

LOGGING = {}
