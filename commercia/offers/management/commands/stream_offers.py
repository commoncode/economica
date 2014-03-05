from django.contrib.webdesign import lorem_ipsum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    # args = '<poll_id poll_id ...>'
    help = 'Stream Offers as the occur'

    def handle(self, *args, **options):

        import zerorpc

        from commercia.offers.models import Offer

        class OfferStream(object):

            @zerorpc.stream
            def offers(self):
                print "called OfferStream.offers"
                # return Offer.objects.all().values()
                return [1, 2, 3, 4]


        s = zerorpc.Server(OfferStream())
        print("Binding zerorpc server to tcp://0.0.0.0:4242")
        s.bind("tcp://0.0.0.0:4242")
        print("run...")
        s.run()
