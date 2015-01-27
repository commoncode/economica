from django.apps import AppConfig
from django.conf import settings
from django.utils.importlib import import_module


class QuotesConfig(AppConfig):
    name = 'quotes'
    verbose_name = 'Quotes'

    def ready(self):
        if getattr(settings, 'CQRS_SERIALIZE'):
            import_module('quotes.collections')
