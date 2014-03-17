from django.contrib.webdesign import lorem_ipsum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ... import factories
from ... import models


class Command(BaseCommand):
    help = 'Create a sample of Cosmetics'

    def handle(self, *args, **options):
        for i in range(20):
            vehicle_instance = factories.VehicleFactory()

            print "GarmentInstance: %s :: title: %s" % (
                vehicle_instance,
                vehicle_instance.title)
