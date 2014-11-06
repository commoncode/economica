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

        for product in Product.objects.all():
            offer = factories.OfferFactory()
            offer.collections.add(*random.sample(
                collections, random.randint(2, top_limit))
            )
            resource = factories.OfferResourceFactory(resource=product)
            factories.OfferResourceContractFactory(
                offer=offer, resource=resource
            )
