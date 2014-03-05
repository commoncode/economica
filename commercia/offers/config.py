from django.apps import AppConfig
from django.utils.importlib import import_module

class OffersConfig(AppConfig):
    name = 'commercia.offers'
    verbose_name = "Offers"

    def ready(self):
        import_module('commercia.offers.collections')
        import_module('commercia.offers.signals')