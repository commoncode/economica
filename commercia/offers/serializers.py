from rest_framework import serializers

from cqrs.serializers import CQRSSerializer
from commercia.products.models import Category
from rea_serializers.serializers import ResourceSerializer

from . import models


class CollectionSerializer(CQRSSerializer):
    class Meta:
        model = models.Collection


class OfferResourceContractSerializer(CQRSSerializer):
    resource = ResourceSerializer()

    class Meta:
        model = models.OfferResourceContract
        exclude = 'offer',


class OfferSerializer(CQRSSerializer):
    collections = CollectionSerializer(many=True, read_only=True)
    discount = serializers.IntegerField(source='discount', read_only=True)
    price = serializers.FloatField(source='price', read_only=True)
    quantity = serializers.IntegerField(source='quantity', read_only=True)
    resource_contracts = OfferResourceContractSerializer(many=True)

    class Meta:
        model = models.Offer
        exclude = 'enabled', 'start', 'end'
