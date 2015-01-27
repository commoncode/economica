from django.core.management.base import BaseCommand
from django.utils.six.moves import input

from ...models import Offer, OfferResource, OfferResourceContract


class Command(BaseCommand):
    help = 'Remove all sample of Offers'

    def handle(self, *args, **options):
        confirm = input(
            'Do you really want to remove all the Offers? '
            'Type \'yes\' to continue, \'no\' to cancel. '
        )

        if confirm == 'yes':
            OfferResourceContract.objects.all().delete()
            OfferResource.objects.all().delete()
            Offer.objects.all().delete()
            print('Offers removed')
