from random import randint

from django.core.management.base import BaseCommand

from commercia.fakers import cosmetics, meals, garments, software, vehicles

from ...factories import CollectionFactory


class Command(BaseCommand):
    args = '<type> [quantity]'
    help = (
        'Collection types: cosmetic | food | garment | software | vehicle'
    )

    def handle(self, *args, **options):
        try:
            faker = {
                'cosmetic': cosmetics,
                'food': meals,
                'garment': garments,
                'software': software,
                'vehicle': vehicles
            }.get(args[0].lower())
        except IndexError:
            faker = None

        try:
            quantity = int(args[1])
        except IndexError:
            quantity = randint(3, 6)

        for i in range(quantity):
            try:
                collection = CollectionFactory(
                    title=faker.words(randint(2, 6)).title()
                )
            except AttributeError:
                collection = CollectionFactory()

            print('Collection: {}'.format(collection))
