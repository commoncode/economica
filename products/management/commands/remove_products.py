from django.core.management.base import BaseCommand
from django.utils.six.moves import input

from ...models import Product, Variant, VariantAspect


class Command(BaseCommand):
    help = 'Remove all Products'

    def handle(self, *args, **options):
        confirm = input(
            'Do you really want to remove all the Products? '
            'Type \'yes\' to continue, \'no\' to cancel. '
        )

        if confirm == 'yes':
            VariantAspect.objects.all().delete()
            Variant.objects.all().delete()
            Product.objects.all().delete()
            print('Offers removed')
