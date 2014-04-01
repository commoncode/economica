from django.apps import AppConfig
from django.utils.importlib import import_module

class QuotesConfig(AppConfig):
    name = 'commercia.quotes'
    verbose_name = "Quotes"

    def ready(self):
        import_module('commercia.quotes.collections')
        # import_module('commercia.quotes.signals')