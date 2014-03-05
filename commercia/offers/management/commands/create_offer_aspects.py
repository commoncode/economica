from django.contrib.webdesign import lorem_ipsum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models


class Command(BaseCommand):

    help = 'Create a sample of Offers Aspects'

    def handle(self, *args, **options):

        offers = models.Offer.objects.all()

        for offer in offers:

            onfo_instance = factories.OfferNForOneFactory(
                offer=offer)
            print "OfferNForOneFactory: %s :: title: %s" % (
                onfo_instance,
                onfo_instance.title)

            # Calling save so we trigger the collection
            # serialization
            onfo_instance.offeraspect_ptr.save()

            od_instance = factories.OfferDiscountFactory(
                offer=offer)
            print "OfferDiscountFactory: %s :: title: %s" % (
                od_instance,
                od_instance.title)

            od_instance.offeraspect_ptr.save()
