from django.apps import AppConfig
from django.conf import settings
from django.utils.importlib import import_module


class OffersConfig(AppConfig):
    name = 'offers'
    verbose_name = 'Offers'

    def ready(self):
        if getattr(settings, 'CQRS_SERIALIZE'):
            import_module('offers.collections')
