import os

from django.core.exceptions import ImproperlyConfigured

import cbs
try:
    import djcelery
except ImportError:
    # Django is running on Local Mode
    pass


DEFAULT_ENV_PREFIX = 'DJANGO_'


class BaseSettings(cbs.BaseSettings):
    # General Settings
    PROJECT_NAME = 'economica'

    # Email Settings
    DEFAULT_FROM_EMAIL = 'Economica <noreply@commoncode.com.au>'
    SERVER_EMAIL = 'Economica <noreply@commoncode.com.au>'
    SEND_BROKEN_LINK_EMAILS = True

    # Security Settings
    SECRET_KEY = 'j$&pgre2x3kz-t-0w-g#js*i#md!id9xfy%e&_w83$)1g$3p2*'

    # CQRS Settings
    CQRS_SERIALIZE = False

    @property
    def MIDDLEWARE_CLASSES(self):
        return (
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        )

    @property
    def INSTALLED_APPS(self):
        contrib = (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        )

        third_party = (
            # Any third party apps
            'cqrs',
            'entropy',
            'images',
            'rea',
            'rea_serializers',
            'rea_patterns_b2c.patterns.salesorder',
        )

        local = (
            # Put here the project's apps
            'offers',
            'products',
            'quotes',
        )

        return contrib + third_party + local


class LocalSettings(BaseSettings):
    INTERNAL_IPS = ('127.0.0.1', )

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(LocalSettings, self).MIDDLEWARE_CLASSES + (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        )

    @property
    def INSTALLED_APPS(self):
        return super(LocalSettings, self).INSTALLED_APPS + (
            'debug_toolbar',
            'django_extensions',
        )


class StagingSettings(BaseSettings):
    try:
        djcelery.setup_loader()
    except NameError:
        # djcelery not found
        pass

    ALLOWED_HOSTS = ['staging.economica.io']

    BROKER_URL = (
        'amqp://economica_staging:economica_staging@'
        'queue.commoncode.com.au:5672/economica_staging'
    )
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'localhost:11211'
        }
    }

    @property
    def INSTALLED_APPS(self):
        return super(StagingSettings, self).INSTALLED_APPS + ('djcelery', )

    @property
    def DATABASES(self):
        return {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'economica_staging',
                'USER': 'economica',
                'PASSWORD': self.db_pass,
                'HOST': self.db_host,
                'PORT': self.db_port,
            }
        }

    @cbs.env(key='DATABASE_PASSWORD')
    def db_pass(self):
        raise ImproperlyConfigured(
            'The DJANGO_DATABASE_PASSWORD environment variable must be set '
            'when using Production or Staging settings.'
        )

    @cbs.env(key='DATABASE_HOST')
    def db_host(self):
        raise ImproperlyConfigured(
            'The DJANGO_DATABASE_HOST environment variable must be set when '
            'using Production or Staging settings.'
        )

    @cbs.env(key='DATABASE_PORT')
    def db_port(self):
        return '5432'


class ProductionSettings(StagingSettings):
    ALLOWED_HOSTS = ['economica.io']

    DEBUG = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(LocalSettings, self).MIDDLEWARE_CLASSES + (
            'iobot.middleware.IOBotMiddleware',
        )

    @cbs.env(key='SECRET_KEY')
    def SECRET_KEY(self):
        raise ImproperlyConfigured(
            'The DJANGO_SECRET_KEY environment variable must be set when '
            'using Production settings.'
        )


# Invoke the settings using the DJANGO_MODE environment variable
MODE = os.environ.get('DJANGO_MODE', 'Local')
cbs.apply('{}Settings'.format(MODE.title()), globals())
