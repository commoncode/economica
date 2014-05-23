from random import randint

from django.core.management.base import BaseCommand

from ...factories import CollectionFactory


class Command(BaseCommand):
    help = 'Create Categories and add products'

    def handle(self, *args, **options):
        for i in range(randint(2, 6)):
            collection = CollectionFactory()
            print 'Collection: {}'.format(collection)
