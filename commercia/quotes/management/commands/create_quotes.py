from django.core.management.base import BaseCommand, CommandError

from ... import factories


class Command(BaseCommand):
    help = 'Create a sample of Quotes'

    def handle(self, *args, **options):
        for i in range(20):
            quote_instance = factories.QuoteFactory

            print "Quote: {}".format(quote_instance.pk)
