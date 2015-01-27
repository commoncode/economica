from django.core.management.base import BaseCommand
from django.utils.six.moves import input

from ...models import Category


class Command(BaseCommand):
    help = 'Clean up Categories'

    def handle(self, *args, **options):
        confirm = input(
            'Do you really want to remove all the Categories? '
            'Type \'yes\' to continue, \'no\' to cancel. '
        )

        if confirm == 'yes':
            Category.objects.all().delete()
            print('Categories removed')
