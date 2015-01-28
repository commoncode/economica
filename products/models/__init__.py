from django.db import models

from images.mixins import ImageMixin

from rea.models import Resource

from .variants import (
    Variant,
    VariantAspect,
    VariantColorAspect,
    VariantShadeAspect,
    VariantSizeAspect
)


'''
The Economica Product Libraries

EntityAspect for Custom Products.

'''


class Product(Resource, ImageMixin):
    '''
    Economica Product.

    The Product model is expected to be sub classed by a Domain Specific
    model. Currently, Economica defines a selection of Archetype Products,
    such as Book, Cosmetic, Garment and so on.
    It's further expected that the Enterprise might provide its own sub
    classed definitions, such as EnterpriseBook.

    '''

    # title
    # slug

    # category = models.ForeignKey('Category', related_name='products')
    description = models.TextField(blank=True)
    sku = models.CharField(blank=True, max_length=512)


#
# Products
#

class Book(Product):
    # title
    # slug
    # category
    # sku

    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    isbn = models.CharField(blank=True, max_length=512)
    year = models.DateField()


class Cosmetic(Product):
    # title
    # slug
    # category
    # sku

    pass


class Food(Product):
    # title
    # slug
    # category
    # sku

    pass


class Garment(Product):
    # title
    # slug
    # category
    # sku

    pass


class Session(Product):
    # title
    # slug
    # category
    # sku

    pass


class Software(Product):
    class License:
        FREEWARE = 0
        SHAREWARE = 1
        TRIALWARE = 2

    LICENSES_CHOICES = (
        (License.FREEWARE, 'Freeware'),
        (License.SHAREWARE, 'Shareware'),
        (License.TRIALWARE, 'Trialware'),
    )

    # title
    # slug
    # category
    # sku

    author = models.CharField(max_length=255)
    license = models.PositiveSmallIntegerField(choices=LICENSES_CHOICES)


class Vehicle(Product):
    # title
    # slug
    # category
    # sku

    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.DateField()
