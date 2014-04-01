from . import models

from cqrs.serializers import CQRSPolymorphicSerializer



class VariantAspectSerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = models.VariantAspect


class VariantSerlizer(CQRSPolymorphicSerializer):

    aspects = VariantAspectSerializer(many=True)

    class Meta:
        model = models.Variant


class ProductSerializer(CQRSPolymorphicSerializer):

    variants = VariantSerlizer(many=True)

    class Meta:
        model = models.Product
