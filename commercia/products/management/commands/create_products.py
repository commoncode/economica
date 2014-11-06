from random import randint

from django.core.management.base import BaseCommand

from ... import factories


class Command(BaseCommand):
    args = '<type> [quantity]'
    help = (
        'Product types: book | cosmetic | food | garment | software | vehicle'
    )

    def handle(self, *args, **options):
        try:
            factory = {
                'book': factories.BookFactory,
                'cosmetic': factories.CosmeticFactory,
                'food': factories.FoodFactory,
                'garment': factories.GarmentFactory,
                'software': factories.SoftwareFactory,
                'vehicle': factories.VehicleFactory
            }.get(args[0].lower())
        except IndexError:
            return (
                'Please declare a type of product, read help for available '
                'options.'
            )

        try:
            quantity = int(args[1])
        except IndexError:
            quantity = randint(20, 30)

        try:
            products = []

            print('Creating Products')

            for i in range(quantity):
                product = factory()
                products.append(product)
                print('{}: {}'.format(args[0].title(), product))
        except ValueError:
            return 'Run create_categories first.'
        except TypeError:
            return 'Product type not available'

        print('Adding Variants')

        for product in products:
            variant = factories.VariantFactory(product=product)

            for i in range(randint(2, 4)):
                factories.VariantColorAspectFactory(variant=variant)
                factories.VariantSizeAspectFactory(variant=variant)
