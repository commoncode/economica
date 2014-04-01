from django.core.management.base import BaseCommand, CommandError

from ... import factories


class Command(BaseCommand):
    help = 'Create a sample of QuoteItems'

    def handle(self, *args, **options):
        for i in range(20):
            quote_item_instance = factories.QuoteItemFactory

            print "QuoteItem: {}".format(quote_item_instance.pk)
