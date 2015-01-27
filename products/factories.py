from datetime import date
import random
import string

import factory

from django.utils.text import slugify

from fakers import cosmetics, garments, lorem_ipsum, meals, software, vehicles
from .models import Category


def randate(start_year=1920, end_year=2015):
    return date(
        random.randint(start_year, end_year),
        random.randint(1, 12),
        random.randint(1, 28)
    )


def randstring(length=9):
    return ''.join(random.choice(
        string.ascii_uppercase + string.digits
    ) for chart in range(length))


class ProductFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'products.Product'
    FACTORY_DJANGO_GET_OR_CREATE = ('slug', )

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(random.randint(2, 5)).title()
    )
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    category = factory.LazyAttribute(
        lambda o: Category.objects.filter(
            parent__isnull=False
        ).order_by('?').first()
    )
    sku = factory.LazyAttribute(
        lambda o: randstring()
    )

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
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(random.randint(2, 5)).title()
    )
    description = factory.LazyAttribute(
        lambda o: lorem_ipsum.paragraphs(random.randint(2, 5))
    )
    genre = factory.LazyAttribute(lambda o: randstring())
    isbn = factory.LazyAttribute(lambda o: randstring())
    year = factory.LazyAttribute(lambda o: randate())


class CosmeticFactory(ProductFactory):
    FACTORY_FOR = 'products.Cosmetic'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(
        lambda o: cosmetics.words(random.randint(2, 5)).title()
    )
    description = factory.LazyAttribute(
        lambda o: cosmetics.paragraphs(random.randint(2, 5))
    )


class FoodFactory(ProductFactory):
    FACTORY_FOR = 'products.Food'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(
        lambda o: meals.words(random.randint(2, 5)).title()
    )
    description = factory.LazyAttribute(
        lambda o: meals.paragraphs(random.randint(2, 5))
    )


class GarmentFactory(ProductFactory):
    FACTORY_FOR = 'products.Garment'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(
        lambda o: garments.words(random.randint(2, 5)).title()
    )
    description = factory.LazyAttribute(
        lambda o: garments.paragraphs(random.randint(2, 5))
    )


class SessionFactory(ProductFactory):
    FACTORY_FOR = 'products.Session'


class SoftwareFactory(ProductFactory):
    FACTORY_FOR = 'products.Software'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(
        lambda o: software.words(random.randint(2, 5)).title()
    )
    description = factory.LazyAttribute(
        lambda o: software.paragraphs(random.randint(2, 5))
    )
    license = factory.LazyAttribute(lambda o: random.randint(0, 2))


class VehicleFactory(ProductFactory):
    FACTORY_FOR = 'products.Vehicle'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(
        lambda o: vehicles.words(random.randint(2, 5)).title()
    )
    description = factory.LazyAttribute(
        lambda o: vehicles.paragraphs(random.randint(2, 5))
    )
    year = factory.LazyAttribute(lambda o: randate())


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
        lambda o: lorem_ipsum.words(random.randint(2, 5)).title()
    )


# @@@ TODO move these factories to the qualites app
class Color(AspectQualityFactory):
    FACTORY_FOR = 'products.Color'

    hex = factory.LazyAttribute(
        lambda o: '#{:02X}{:02X}{:02X}'.format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )


class Size(AspectQualityFactory):
    FACTORY_FOR = 'products.Size'

    dimension = factory.LazyAttribute(
        lambda o: random.choice(['Centimeter', 'Foot', 'Inch', 'Yard'])
    )
    measure = factory.LazyAttribute(lambda o: random.randint(1, 12))


class VariantColorAspectFactory(VariantAspectFactory):
    FACTORY_FOR = 'products.VariantColorAspect'
    FACTORY_DJANGO_GET_OR_CREATE = ('variant', 'color')

    color = factory.SubFactory(Color)


class VariantSizeAspectFactory(VariantAspectFactory):
    FACTORY_FOR = 'products.VariantSizeAspect'
    FACTORY_DJANGO_GET_OR_CREATE = ('variant', 'size')

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
