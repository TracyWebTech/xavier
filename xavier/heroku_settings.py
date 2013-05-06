import os
from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = os.path.dirname(__file__)

ADMINS = ADMINS = (
    ('Tracy SysAdmin', 'sysadmin@tracy.com.br'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost')
}

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/tmp/media/'
STATIC_ROOT = '/tmp/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('SECRET_KEY', '')

LOGGING['handlers']['mail_admins']['include_html'] = True
