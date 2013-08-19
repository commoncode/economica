from economica.settings.common import *
from economica.settings.local import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = [
    '127.0.0.1',
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}


MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    'debug_toolbar',
    'devserver',
    'django_extensions',
]

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'runtime', 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'resources', 'static')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(PROJECT_ROOT, 'runtime', 'cache')
    }
}

# For test speedup purposes.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.SHA1PasswordHasher',
]

# Time
USE_TZ = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_ROOT + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
        'platforms': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}