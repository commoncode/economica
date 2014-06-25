from rest_framework import serializers

from cqrs.serializers import CQRSPolymorphicSerializer, CQRSSerializer

from images.serializers import ImageInstanceSerializer
from .models import AspectQuality, Category, Product, Variant, VariantAspect


class ParentCategorySerializer(serializers.ModelSerializer):
    '''Returns one level of parent category up...'''

    class Meta:
        model = Category


class CategorySerializer(CQRSSerializer):
    parent = ParentCategorySerializer()

    class Meta:
        model = Category


class AspectQualitySerializer(CQRSPolymorphicSerializer):
    class Meta:
        model = AspectQuality


class VariantAspectSerializer(CQRSPolymorphicSerializer):
    class Meta:
        model = VariantAspect


class VariantSerlizer(CQRSSerializer):
    aspects = VariantAspectSerializer(many=True)

    class Meta:
        model = Variant


class ProductSerializer(CQRSPolymorphicSerializer):
    category = CategorySerializer()
    images = ImageInstanceSerializer(many=True)
    variants = VariantSerlizer(many=True)

    class Meta:
        model = Product
