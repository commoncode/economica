from django.contrib.webdesign import lorem_ipsum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models


class Command(BaseCommand):

    # args = '<poll_id poll_id ...>'
    help = 'Create a sample of Offers'

    def handle(self, *args, **options):

        i = 0
        while i < 10:
            offer_instance = factories.OfferFactory()
            print "OfferInstance: %s :: title: %s" % (
                offer_instance,
                offer_instance.title)

            # onfo_instance = factories.OfferNForOneFactory()
            # print "OfferNForOneFactory: %s :: title: %s" % (
            #     onfo_instance,
            #     onfo_instance.title)

            i+=1

# 
        # offers = models.Offer.objects.all()

        for offer in offers:
            print "Adding Resource Contract: %s " % (offer.title)
            
            orc_instance = factories.OfferResourceContractFactory(offer=offer)
            print "Added: %s" % orc_instance

            print "Altering tittle of: %s" % orc_instance
            offer.title = lorem_ipsum.words(3, common=False).title()
            print "To: %s" % offer.title
            offer.save()

        # for offer in offers:
        #     print "Adding Offer Aspect: %s " % (offer.title)

        #     oad_instance = factories.OfferDiscountFactory(
        #         offer=offer)


        offers.delete()



