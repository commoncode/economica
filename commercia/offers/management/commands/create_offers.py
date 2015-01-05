import random

from django.core.management.base import BaseCommand

from commercia.products.models import Product

from ...models import Collection
from ... import factories


class Command(BaseCommand):
    help = 'Create a sample of Offers'

    def handle(self, *args, **options):
        collections = Collection.objects.all()

        if not collections.exists():
            return 'Please run ./manage.py create_collections [type] [number]'

        top_limit = len(collections)
        top_limit = 3 if top_limit > 3 else top_limit

        for product in Product.objects.all():
            offer = factories.OfferFactory()
            offer.collections.add(*random.sample(
                collections, random.randint(1, top_limit)
            ))

            resource = factories.OfferResourceFactory(
                offer=offer, resource=product
            )
            factories.OfferResourceContractFactory(
                offer=offer, resource=resource
            )
            factories.OfferPriceFactory(offer=offer)
            factories.OfferNForOneFactory(offer=offer)

            if bool(random.getrandbits(1)):
                factories.OfferDiscountFactory(offer=offer)

            offer.save()
