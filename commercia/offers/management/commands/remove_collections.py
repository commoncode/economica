from django.core.management.base import BaseCommand
from django.utils.six.moves import input

from ...models import Collection


class Command(BaseCommand):
    help = 'Remove all sample of Collections'

    def handle(self, *args, **options):
        confirm = input(
            'Do you really want to remove all the Collections? '
            'Type \'yes\' to continue, \'no\' to cancel. '
        )

        if confirm == 'yes':
            Collection.objects.all().delete()
            print('Collections removed')
