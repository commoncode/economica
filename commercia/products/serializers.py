from rest_framework import serializers

from cqrs.serializers import CQRSPolymorphicSerializer, CQRSSerializer

from images.serializers import ImageInstanceSerializer
from . import models


class CategorySerializer(CQRSSerializer):

    class Meta:
        model = models.Category


class AspectQualitySerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = models.AspectQuality


class VariantAspectSerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = models.VariantAspect


class VariantSerlizer(CQRSSerializer):

    aspects = VariantAspectSerializer(
        many=True)

    class Meta:
        model = models.Variant


class ProductSerializer(CQRSPolymorphicSerializer):

    category = CategorySerializer()

    images = ImageInstanceSerializer(
        many=True)

    variants = VariantSerlizer(
        many=True)

    class Meta:
        model = models.Product
