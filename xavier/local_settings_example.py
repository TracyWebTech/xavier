import os
from settings import *

PROJECT_DIR = os.path.dirname(__file__)
TEST_PEP8_DIRS = [os.path.dirname(PROJECT_DIR), ]
TEST_PEP8_EXCLUDE = ['migrations', 'urls.py']

INSTALLED_APPS += ('test_pep8', )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/tmp/media/'
STATIC_ROOT = '/tmp/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '123'

try:
    import django_extensions
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        'django_extensions',
    )

try:
    import devserver
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        'devserver',
    )
    MIDDLEWARE_CLASSES += (
        'devserver.middleware.DevServerMiddleware',
    )

try:
    import debug_toolbar
except ImportError:
    pass
else:
    INTERNAL_IPS = ('127.0.0.1', '192.168.56.1')
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False
    }
