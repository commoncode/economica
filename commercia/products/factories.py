import datetime
import factory

from django.contrib.webdesign import lorem_ipsum

from fakers import lipservice, cosmetics, garments, vehicles

from faker import Factory


fake = Factory.create()


class ProductFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'products.Product'

    title = factory.LazyAttribute(
        lambda o: lipservice.words(5, common=False).title())

    @factory.post_generation
    def variants(self, create, extracted, **kwargs):

        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of variants were passed in, use them
            for variant in extracted:
                self.variants.add(variant)

# 
# Product Factories
#

class BookFactory(ProductFactory):
    FACTORY_FOR = 'products.Book'

    isbn = '1234567890'


class CosmeticFactory(ProductFactory):
    FACTORY_FOR = 'products.Cosmetic'

    title = factory.LazyAttribute(
        lambda o: cosmetics.words(3, common=False).title())


class FoodFactory(ProductFactory):
    FACTORY_FOR = 'products.Food'


class GarmentFactory(ProductFactory):
    FACTORY_FOR = 'products.Garment'

    title = factory.LazyAttribute(
        lambda o: garments.words(3, common=False).title())


class SoftwareFactory(ProductFactory):
    FACTORY_FOR = 'products.Software'


class VehicleFactory(ProductFactory):
    FACTORY_FOR = 'products.Vehicle'

    title = factory.LazyAttribute(
        lambda o: vehicles.words(3, common=False).title())

    # make
    # model
    # registration


#
# Product Variants
#


class VariantFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'products.Variant'

    product = factory.SubFactory(ProductFactory)



