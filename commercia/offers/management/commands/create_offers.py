from random import choice, randint

from django.contrib.webdesign import lorem_ipsum
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models


class Command(BaseCommand):
    help = 'Create a sample of Offers'

    def handle(self, *args, **options):
        collections = models.Collection.objects.all()

        if not collections.exists():
            call_command('create_collections')

        for i in range(randint(5, 10)):
            offer = factories.OfferFactory(collection=choice(collections))
            print 'Offer: {}'.format(offer)

            orc = factories.OfferResourceContractFactory(offer=offer)
            print 'Added: {}'.format(orc)

            onfo = factories.OfferNForOneFactory(offer=offer)
            print 'Added: {}'.format(onfo)

            offer.save()
