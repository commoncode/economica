from random import choice, randint

from django.core.management.base import BaseCommand

from commercia.offers.models import Offer

from ...factories import CollectionFactory, CategoryFactory
from ...models import Product


class Command(BaseCommand):
    help = 'Create Categories and add products'

    def handle(self, *args, **options):
        products = Product.objects.all()

        for i in range(randint(6, 9)):
            collection = CollectionFactory()

            for j in range(randint(2, 5)):
                category = CategoryFactory(collection=collection)

                for k in range(randint(1, 3)):
                    product = choice(products)
                    product.categories.add(category)
                    product.save()

                    print 'Added category {} to product {}'.format(
                        category.title, product.title)

                category.save()

                print 'Category: {}'.format(category.title)

            collection.save()

            print 'Collection: {}'.format(collection.title)

        for offer in Offer.objects.all():
            offer.save()
