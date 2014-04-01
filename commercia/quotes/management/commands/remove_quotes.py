from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models


class Command(BaseCommand):

    help = 'Remove all sample of Quotes'

    def handle(self, *args, **options):

        models.Quote.objects.all().delete()