import random

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models

PRODUCT_FACTORIES = (
    factories.BookFactory,
    factories.CosmeticFactory,
    factories.FoodFactory,
    factories.GarmentFactory,
    factories.SoftwareFactory,
    factories.VehicleFactory,
)

class Command(BaseCommand):

    # args = '<poll_id poll_id ...>'
    help = 'Create a sample of Products'

    def handle(self, *args, **options):

        factories.Color()

        for i in range(5):

            product_factory = PRODUCT_FACTORIES[
                random.randrange(0, len(PRODUCT_FACTORIES))
            ]

            product_instance = product_factory()

            print "Product: %s :: title: %s" % (
                product_instance.__class__,
                product_instance.title)

            variant_instance = factories.VariantFactory(product=product_instance.product)
            print "Added Variant %s to product %s" % (
                variant_instance,
                product_instance)

            variant_color_aspect_instance = factories.VariantColorAspectFactory(
                variant = variant_instance)

            print "Added Variant Color Aspect %s to variant %s" % (
                variant_color_aspect_instance.color.hex,
                variant_instance)

            variant_size_aspect_instance = factories.VariantSizeAspectFactory(
                variant = variant_instance)

            print "Added Variant Size Aspect %s to variant %s" % (
                variant_size_aspect_instance.size.dimension,
                variant_instance)

            product_instance.product.save()
