from django.apps import AppConfig
from django.conf import settings
from django.utils.importlib import import_module


class ProductsConfig(AppConfig):
    name = 'products'
    verbose_name = 'Products'

    def ready(self):
        if getattr(settings, 'CQRS_SERIALIZE'):
            import_module('products.collections')
