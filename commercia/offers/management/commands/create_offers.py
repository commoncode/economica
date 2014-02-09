from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ... import factories

class Command(BaseCommand):

    # args = '<poll_id poll_id ...>'
    help = 'Create a sample of Offers'

    def handle(self, *args, **options):

        i = 0
        while i < 10:
            offer_instance = factories.OfferFactory()
            print "OfferInstance: %s :: date: %s" % (
                offer_instance,
                offer_instance.title)
            i+=1