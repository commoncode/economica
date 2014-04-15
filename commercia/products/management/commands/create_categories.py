from random import choice, randint

from django.core.management.base import BaseCommand

from commercia.offers.models import Offer

from ...factories import CategoryFactory
from ...models import Product


class Command(BaseCommand):
    help = 'Create Categories and add products'

    def handle(self, *args, **options):
        products = Product.objects.all()

        for i in range(randint(5, 10)):
            category = CategoryFactory()

            for j in range(randint(2, 5)):
                product = choice(products)
                product.categories.add(category)
                product.save()

                print 'Added category {} to product {}'.format(category.title,
                    product.title)

            print 'Category: {}'.format(category.title)

        for offer in Offer.objects.all():
            offer.save()
