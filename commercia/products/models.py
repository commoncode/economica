from django.db import models

from cqrs.models import CQRSModel, CQRSPolymorphicModel
from entropy.base import EnabledMixin, SlugMixin, TitleMixin
from images.mixins import ImageMixin

from rea.models import Resource
from rea.settings import REA_PROVIDING_AGENT_MODEL


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

    category = models.ForeignKey('Category', related_name='products')
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


# Variants

class Variant(CQRSModel):
    '''
    Product Variant.

    Products define at least one Variant.

    '''

    product = models.ForeignKey('Product', related_name='variants')


# Variant Aspects

class VariantAspect(CQRSPolymorphicModel):
    variant = models.ForeignKey('Variant', related_name='aspects')


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
    # title
    # slug

    pass


class Color(AspectQuality):
    hex = models.CharField(max_length='6')

    '''
    def hsv(self):
        return h, s, v

    def rgb(self):
        return r, g, b

    def hsl(self):
        return h, s, l

    def name
        determine the name from some kinda color chart
    '''


class Size(AspectQuality):
    # title
    # short_title
    # slug

    dimension = models.CharField(max_length=512)
    measure = models.CharField(max_length=128)


class Property(AspectQuality):
    # title
    # short_title
    # slug

    value = models.CharField(max_length=256)


#
# Variant Templates
#

class VariantTemplate(CQRSModel):
    '''
    Variant Templates are used to define re-usable
    template patterns for Variants, VariantAspects &
    Variant Aspect Qualities.

    '''

    agent = models.ForeignKey(REA_PROVIDING_AGENT_MODEL)
    product = models.ForeignKey('contenttypes.ContentType')
    # XXX limit choices to ContentTypes that are a child
    # to Product.


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
    # title
    # slug
    # is_enabled

    parent = models.ForeignKey('self', null=True, related_name='children')

    def __unicode__(self):
        return self.title


# TODO Create an abstract pattern to express the re-usable Aspect /
# AspectInstance / AspectRule pattern
class SmartCollection(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    '''
    A collection of objects according to specified aspect rules.

    Either Products or Offers

    '''

    # title
    # slug
    # is_enabled

    pass


class SmartCollectionAspectInstance(CQRSModel):
    entity = models.ForeignKey('SmartCollection')
    aspect = models.ForeignKey('SmartCollectionAspect')


class SmartCollectionAspectRule(CQRSModel):
    pass


class SmartCollectionAspect(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    # title
    # slug
    # is_enabled

    rules = models.ForeignKey('SmartCollectionAspectRule')
