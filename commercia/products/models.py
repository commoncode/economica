from django.db import models

from cqrs.mongo import CQRSModel, CQRSPolymorphicModel
from entropy.base import (
    EnabledMixin, SlugMixin, TitleMixin
)

from rea.models import Resource


'''
EntityAspect for Custom Products.
The Economica Product Libraries

'''


class Product(Resource):
    '''
    Economica Product

    Classifications

        + Tangible
        + Intangible

    '''

    is_tangible = models.BooleanField(default=True)


# Products

class Book(Product):
    pass

class Garment(Product):
    pass

class Cosmetic(Product):
    '''

    '''
    
    shades = models.ManyToManyField('Color')


# Variants

class Variant(CQRSModel):
    
    product = models.ForeignKey('Product')


# Variant Aspects

class VariantAspect(CQRSPolymorphicModel):
    
    variant = models.ForeignKey('Variant')


class VariantSizeAspect(VariantAspect):
    pass


class VariantShadeAspect(VariantAspect):
    pass


class VariantColorAspect(VariantAspect):
    pass


# Variant Aspect Qualities

class Color(CQRSModel, SlugMixin, TitleMixin):
    
    hex = models.CharField(
        max_length='6')

    # def hsv(self):
        # return h, s, v

    # def rgb(self):
        # return r, g, b

    # def hsl(self):
        # return h, s, l


class Size(CQRSModel):
    pass

class Property(CQRSModel):
    '''
    Cover: hard or soft
    '''
    pass


# Categories

class Category(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    
    parent = models.ForeignKey('self')


    def children(self):
        return Category.objects.filter(parent__id=self.id)


class Collection(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    '''
    An arbitrary Collection of Offers according to Promotional themes.
    '''
    pass


# Collections

# TODO Create an abstract pattern to express the re-usable Aspect / 
# AspectInstance / AspectRule pattern
class SmartCollection(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    '''
    A collection of objects according to specified aspect rules.

    Either Products or Offers
    '''
    pass

class SmartCollectionAspectInstance(CQRSModel):

    entity = models.ForeignKey('SmartCollection')
    aspect = models.ForeignKey('SmartCollectionAspect')


class SmartCollectionAspectRule(CQRSModel):
    pass


class SmartCollectionAspect(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    
    rules = models.ForeignKey('SmartCollectionAspectRule')
