import random

from django.contrib.webdesign import lorem_ipsum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models


class Command(BaseCommand):

    # args = '<poll_id poll_id ...>'
    help = 'Create a sample of Variants'

    def handle(self, *args, **options):

        products = models.Product.objects.all()
        for product in products:

            variant_instance = factories.VariantFactory(product=product)
            print "Added Variant %s to product %s" % (
                variant_instance,
                product)

