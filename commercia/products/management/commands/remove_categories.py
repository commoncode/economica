from django.core.management.base import BaseCommand

from ...models import Category


class Command(BaseCommand):
    help = 'Clean up Menus'

    def handle(self, *args, **options):
        Category.objects.all().delete()
