from django.apps import AppConfig
from django.utils.importlib import import_module

class ProductsConfig(AppConfig):
    name = 'commercia.products'
    verbose_name = "Products"

    def ready(self):
        import_module('commercia.products.collections')
        # import_module('commercia.products.signals')