from economica.settings.common import *

import djcelery


djcelery.setup_loader()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'economica_staging',
        'USER': 'economica',
        'PASSWORD': 'hgSDfgoi3dg',
        'HOST': 'commoncode.cupxs40in6f6.ap-northeast-1.rds.amazonaws.com',
        'PORT': '',
    }
}

INSTALLED_APPS += ('djcelery', )

BROKER_URL = (
    'amqp://economica_staging:economica_staging@queue.commoncode.com.au:5672/'
    'economica_staging'
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), 'files', 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), 'static')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211'
    },
}
