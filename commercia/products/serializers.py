from datetime import datetime

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


class VariantSerializer(CQRSSerializer):
    aspects = VariantAspectSerializer(many=True)

    class Meta:
        model = Variant


class ProductSerializer(CQRSPolymorphicSerializer):
    category = CategorySerializer()
    images = ImageInstanceSerializer(many=True)
    variants = VariantSerializer(many=True)
    year = serializers.SerializerMethodField('year_datetime')

    class Meta:
        model = Product

    def year_datetime(self, obj):
        try:
            return datetime.combine(obj.year, datetime.min.time())
        except AttributeError:
            # Product doesn't have year field
            pass
