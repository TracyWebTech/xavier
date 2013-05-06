import os
import dj_database_url

from settings import *

DEBUG = True
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
MEDIA_ROOT = '/tmp/media/'

STATIC_URL = 'https://s3-sa-east-1.amazonaws.com/xavier-dev/'
STATIC_ROOT = '/tmp/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('SECRET_KEY', '')

ALLOWED_HOSTS = ['xavier.herokuapp.com']

LOGGING['handlers']['mail_admins']['include_html'] = True

INSTALLED_APPS += ('storages', )

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
