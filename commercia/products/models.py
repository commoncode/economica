from django.db import models

from cqrs.models import CQRSModel, CQRSPolymorphicModel
from entropy.base import (
    EnabledMixin, SlugMixin, TitleMixin
)

from rea.models import Resource
from rea.settings import REA_PROVIDING_AGENT_MODEL, REA_REPORTING_AGENT_ID


'''
The Economica Product Libraries


EntityAspect for Custom Products.

'''


class Product(Resource):
    '''
    Economica Product.

    The Product model is expected to be sub classed by a Domain
    Specific model.  Currently, Economica defines a selection of
    Archetype Products, such as Book, Cosmetic, Garment and so on.
    It's further expected that the Enterprise might provide its own
    sub classed definitions, such as EnterpriseBook.

    '''

    sku = models.CharField(
        blank=True,
        max_length=512)

#
# Products
#

class Book(Product):

    isbn = models.CharField(
        blank=True,
        max_length=512)


class Cosmetic(Product):
    pass


class Food(Product):
    pass


class Garment(Product):
    pass


class Session(Product):
    pass


class Software(Product):
    pass


class Vehicle(Product):
    pass

    # make
    # model
    # year


# Variants

class Variant(CQRSModel):
    '''
    Product Variant.

    Products define at least one Variant.
    '''

    product = models.ForeignKey(
        'Product',
        related_name='variants')


# Variant Aspects

class VariantAspect(CQRSPolymorphicModel):

    variant = models.ForeignKey(
        'Variant',
        related_name='aspects')


class VariantSizeAspect(VariantAspect):

    size = models.ForeignKey('Size')


class VariantShadeAspect(VariantAspect):

    shade = models.ForeignKey('Color')


class VariantColorAspect(VariantAspect):

    color = models.ForeignKey('Color')


#
# Aspect Qualities
#

# @@@ push these out to a separate app.
class AspectQuality(CQRSPolymorphicModel, SlugMixin, TitleMixin):
    pass


class Color(AspectQuality):

    hex = models.CharField(
        max_length='6')

    # def hsv(self):
        # return h, s, v

    # def rgb(self):
        # return r, g, b

    # def hsl(self):
        # return h, s, l

    # def name
        # determine the name from some kinda color chart


class Size(AspectQuality):

    # title
    # short_title
    # slug

    dimension = models.CharField(
        max_length=512)
    measure = models.CharField(
        max_length=128)


class Property(AspectQuality):

    # title
    # short_title
    # slug

    value = models.CharField(
        max_length=256)


#
# Variant Templates
#

class VariantTemplate(CQRSModel):
    '''
    Variant Templates are used to define re-usable
    template patterns for Variants, VariantAspects &
    Variant Aspect Qualities.

    '''
    product = models.ForeignKey(
        'contenttypes.ContentType')
    # XXX limit choices to ContentTypes that are a child
    # to Product.

    agent = models.ForeignKey(
        REA_PROVIDING_AGENT_MODEL)


class VariantTemplateAspect(CQRSPolymorphicModel):
    '''
    Variant Aspect related to Variant Template w/ Aspect Qualities
    '''

    variant_template = models.ForeignKey('VariantTemplate')
    variant_aspect = models.ForeignKey('VariantAspect')


class VariantTemplateAspectQuality(CQRSModel):
    '''
    Conjunct the Variant Template Aspect with a Quality.
    '''
    variant_template_aspect = models.ForeignKey('VariantTemplateAspect')
    aspect_quality = models.ForeignKey('AspectQuality')


#
# Categories
#

class Category(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):

    parent = models.ForeignKey('self')


    def children(self):
        return Category.objects.filter(parent__id=self.id)


class Collection(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    '''
    An arbitrary Collection of Offers according to Promotional themes.
    '''
    pass


#
# Collections
#


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
