from django.contrib.webdesign import lorem_ipsum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models


class Command(BaseCommand):

    help = 'Remove all sample of Offers Aspects'

    def handle(self, *args, **options):

        models.OfferAspect.objects.all().delete()