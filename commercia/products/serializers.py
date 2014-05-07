from cqrs.serializers import CQRSPolymorphicSerializer, CQRSSerializer

from . import models


class CategorySerializer(CQRSSerializer):
    class Meta:
        model = models.Category


class AspectQualitySerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = models.AspectQuality


class VariantAspectSerializer(CQRSPolymorphicSerializer):

    # @@@ Only one of these will exist.
    color = AspectQualitySerializer()
    size = AspectQualitySerializer()

    class Meta:
        model = models.VariantAspect

    def field_to_native(self, obj, field_name):
        # Make the incorrect field definitions fail silently
        # yet only if they're in our list
        try:
            super(VariantAspectSerializer, self).field_to_native(obj, field_name)
        except Exception, e:
            # @@@ TODO needs to be caught lower
            # in fields.get_component(obj, attr_name)
            print e



class VariantSerlizer(CQRSSerializer):

    aspects = VariantAspectSerializer(many=True)

    class Meta:
        model = models.Variant


class ProductSerializer(CQRSPolymorphicSerializer):
    variants = VariantSerlizer(many=True)

    class Meta:
        model = models.Product
