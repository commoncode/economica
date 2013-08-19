from infrastruction.settings import *

# Django settings for CommonCode.com.au homepage
import os, re

ADMINS = [
    # ('Your Name', 'your_email@example.com'),
]

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'Economica <noreply@commoncode.com.au>'
SERVER_EMAIL = 'Economica <noreply@commoncode.com.au>'

EMAIL_SUBJECT_PREFIX = '[Economica]'

SEND_BROKEN_LINK_EMAILS = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Australia/Melbourne'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'resources', 'static'),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j$&pgre2x3kz-t-0w-g#js*i#md!id9xfy%e&_w83$)1g$3p2*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    'dynamicloader.loader.load_template_source',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'tracking.middleware.VisitorTrackingMiddleware',
    'platforms.middleware.PlatformResolutionMiddleware',
    'dynamicloader.middleware.RequestMiddleware',
]

ROOT_URLCONF = 'economica.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'economica.wsgi.application'

TEMPLATE_DIRS = [
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'resources', 'templates'),
]

INSTALLED_APPS += [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # for markdown
    'django.contrib.markup',

    # Third party apps
    'south',
    'tastypie', # XXX which API? nap or django-rest?

    # Common Code apps
    'entropy',
    'posts',
    'pages',
    'menus',
    'platforms',

    # Common Code REA
    # 'market', # REA market entities and patterns
    # 'enterprise', # REA enterprise entities and patterns

    # Economica apps
    # 'stores',
    # 'markets',

]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "platforms.context_processors.platform"
]

#######################################
# Third party app settings
#######################################

# Set the custom user model
AUTH_USER_MODEL = 'accounts.User'


# Easy Thumbnails compression options

THUMBNAIL_ALIASES = {
    'accounts.User': {
        'homepage': {
            'size': (220, 200),
            'crop': 'smart',
        },
    },
}

# Posts
POSTS_USE_POSTS_MODEL = True

# Platforms
PLATFORMS_USE_PLATFORMS = True

# Dynamic Template Loader
DYN_TEMPLATE_MAP = {
    'PLATFORM_SLUG': {
        re.compile('common-code'): (
            os.path.join(PROJECT_ROOT, 'resources', 'templates', 'common-code'),
            ),
    },
}