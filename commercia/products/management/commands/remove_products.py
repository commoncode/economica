from django.contrib.webdesign import lorem_ipsum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models


class Command(BaseCommand):

    help = 'Remove all sample of Offers'

    def handle(self, *args, **options):

        products = models.Product.objects.all()

        for product in products:
            try:
                product.delete()
                print 'deleted!'
            except models.Product.DoesNotExist as e:
                print '%s :: %s' % (e, product)
