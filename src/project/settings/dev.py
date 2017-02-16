from project.settings.base import *

SECRET_KEY = 'dev-dev-dev-dev-dev-dev-dev'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE.append(
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

try:
    from project.settings.local import *
except ImportError:
    pass
