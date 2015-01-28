from django.db import models

from cqrs.models import CQRSModel, CQRSPolymorphicModel


#
# Variants
#
class Variant(CQRSModel):
    '''
    Product Variant.

    Products define at least one Variant.

    '''

    product = models.ForeignKey('Product', related_name='variants')

    class Meta:
        app_label = 'products'


#
# Variant Aspects
#
class VariantAspect(CQRSPolymorphicModel):
    variant = models.ForeignKey('Variant', related_name='aspects')

    class Meta:
        app_label = 'products'


class VariantColorAspect(VariantAspect):
    color = models.ForeignKey('aspects.Color')

    class Meta:
        app_label = 'products'


class VariantShadeAspect(VariantAspect):
    shade = models.ForeignKey('aspects.Color')

    class Meta:
        app_label = 'products'


class VariantSizeAspect(VariantAspect):
    size = models.ForeignKey('aspects.Size')

    class Meta:
        app_label = 'products'


"""
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

    class Meta:
        app_label = 'products'


class VariantTemplateAspect(CQRSPolymorphicModel):
    '''
    Variant Aspect related to Variant Template w/ Aspect Qualities

    '''

    variant_template = models.ForeignKey('VariantTemplate')
    variant_aspect = models.ForeignKey('VariantAspect')

    class Meta:
        app_label = 'products'


class VariantTemplateAspectQuality(CQRSModel):
    '''
    Conjunct the Variant Template Aspect with a Quality.

    '''

    variant_template_aspect = models.ForeignKey('VariantTemplateAspect')
    aspect_quality = models.ForeignKey('aspects.AspectQuality')

    class Meta:
        app_label = 'products'
"""
