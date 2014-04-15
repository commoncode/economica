from rest_framework import serializers

from cqrs.serializers import CQRSSerializer, CQRSPolymorphicSerializer
from rea_serializers.serializers import ResourceSerializer

from commercia.products.models import Category
from .models import *


class CategoryArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

    def to_native(self, obj):
        return obj


class OfferResourceContractSerializer(CQRSSerializer):

    resource = ResourceSerializer()

    class Meta:
        model = OfferResourceContract
        fields = (
            'id',
            'contract',
            'resource',
            'quantity'
        )


class OfferSerializer(CQRSSerializer):
    categories = CategoryArraySerializer(source='categories', read_only=True)
    discount = serializers.IntegerField(source='discount', read_only=True)
    price = serializers.FloatField(source='price', read_only=True)
    quantity = serializers.IntegerField(source='quantity', read_only=True)
    resource_contracts = OfferResourceContractSerializer(many=True)

    class Meta:
        model = Offer
        fields = (
            'id',
            'categories',
            'discount',
            'price',
            'quantity',
            'resource_contracts',
            'short_title',
            'title',
        )
