from rest_framework import serializers
from cqrs.serializers import CQRSSerializer, CQRSPolymorphicSerializer
from rea_serializers.serializers import ContractSerializer, ResourceSerializer


from . import models


class CollectionSerializer(CQRSSerializer):

    class Meta:
        model = models.Collection


class OfferResourceContractSerializer(CQRSSerializer):

    contract = ContractSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = models.OfferResourceContract
        fields = (
            'contract',
            'id',
            'quantity',
            'resource',
        )


class OfferAspectSerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = models.OfferAspect


class OfferSerializer(CQRSSerializer):

    collections = CollectionSerializer(
        many=True)

    discount = serializers.IntegerField(
        source='discount',
        read_only=True)

    price = serializers.FloatField(
        source='price',
        read_only=True)

    quantity = serializers.IntegerField(
        source='quantity',
        read_only=True)

    resource_contracts = OfferResourceContractSerializer(many=True)

    offer_aspects = OfferAspectSerializer(many=True)

    class Meta:
        model = models.Offer
        fields = (
            'collections',
            'discount',
            'id',
            'offer_aspects',
            'price',
            'quantity',
            'resource_contracts',
            'short_title',
            'title',
        )
