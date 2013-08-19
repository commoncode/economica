import os

if os.environ.get('DJANGO_DEVELOPMENT'):
    from economica.settings.development import *
