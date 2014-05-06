from random import randint

from django.core.management.base import BaseCommand

from ...factories import CategoryFactory


class Command(BaseCommand):
    help = 'Create Categories and add products'

    def handle(self, *args, **options):
        for i in range(randint(6, 9)):
            category = CategoryFactory()

            for j in range(randint(2, 5)):
                subcategory = CategoryFactory(parent=category)

                print 'Subcategory: {}'.format(subcategory)

            print 'Category: {}'.format(category)
