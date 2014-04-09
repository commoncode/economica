from django.contrib.webdesign import lorem_ipsum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models


class Command(BaseCommand):

    # args = '<poll_id poll_id ...>'
    help = 'Create a sample of Offers'

    def handle(self, *args, **options):
        offers = []

        for i in range(5):
            offer_instance = factories.OfferFactory()
            offers.append(offer_instance)

            print "OfferInstance: %s :: title: %s" % (
                offer_instance,
                offer_instance.title)

        for offer in offers:
            print "Adding Resource Contract: %s " % (offer.title)

            orc_instance = factories.OfferResourceContractFactory(offer=offer)
            print "Added: %s" % orc_instance

            onfo_instance = factories.OfferNForOneFactory(
                offer=offer)
            print "OfferNForOneFactory: %s :: title: %s" % (
                onfo_instance,
                onfo_instance.title)

            offer.save()
