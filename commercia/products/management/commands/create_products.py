from random import choice, randint

from django.conf import settings
from django.core.management import call_command
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
    help = 'Create a sample of Products'

    def handle(self, *args, **options):
        factories.Color()

        categories = models.Category.objects.all()

        if not categories.exists():
            call_command('create_categories')

        for i in range(randint(5, 15)):
            product = choice(PRODUCT_FACTORIES)(category=choice(categories))
            print 'Product: {} :: Title: {} :: Category: {}'.format(
                product.__class__, product.title, product.category)

            variant = factories.VariantFactory(product=product)
            print 'Added Variant {} to product {}'.format(variant, product)

            variant_color_aspect = factories.VariantColorAspectFactory(
                variant=variant)
            print 'Added Variant Color Aspect {} to variant {}'.format(
                variant_color_aspect.color.hex, variant)

            variant_size_aspect = factories.VariantSizeAspectFactory(
                variant=variant)
            print 'Added Variant Size Aspect {} to variant {}'.format(
                variant_size_aspect.size.dimension, variant)

            product.save()
