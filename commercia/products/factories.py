import datetime
import factory
import random

from django.contrib.webdesign import lorem_ipsum
from django.core.management import call_command
from django.template.defaultfilters import slugify

from fakers import lipservice, cosmetics, garments, vehicles
from faker import Factory

from .models import Category

fake = Factory.create()


class ProductFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'products.Product'

    title = factory.LazyAttribute(
        lambda o: lipservice.words(5, common=False).title())

    @factory.lazy_attribute
    def category(self):
        categories = Category.objects.filter(parent__isnull=False)

        if not categories.exists():
            call_command('create_categories')

        return random.choice(categories)

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


class SessionFactory(ProductFactory):
    FACTORY_FOR = 'products.Session'


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


class VariantAspectFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'products.VariantAspect'

    variant = factory.SubFactory(VariantFactory)


class AspectQualityFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'products.AspectQuality'

    title = factory.LazyAttribute(
        lambda o: vehicles.words(3, common=False).title())


# @@@ TODO move these factories to the qualites app
def random_hex():
    return '#%02X%02X%02X' % (
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255))


class Color(AspectQualityFactory):
    FACTORY_FOR = 'products.Color'

    # @@@ TODO overwrite title with a color faker tile

    hex = factory.LazyAttribute(
        lambda o: random_hex())


class Size(AspectQualityFactory):
    FACTORY_FOR = 'products.Size'

    # @@@ TODO make these dynamic fakers
    dimension = 'Foot'
    measure = '12'


class VariantColorAspectFactory(VariantAspectFactory):
    FACTORY_FOR = 'products.VariantColorAspect'

    color = factory.SubFactory(Color)


class VariantSizeAspectFactory(VariantAspectFactory):
    FACTORY_FOR = 'products.VariantSizeAspect'

    size = factory.SubFactory(Size)


#
# Categories
#
class CategoryFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'products.Category'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(random.randint(1, 2), common=False).title()
    )
    slug = factory.LazyAttribute(
        lambda o: slugify(
            lorem_ipsum.words(random.randint(1, 5), common=False)
        )
    )
