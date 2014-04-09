from rest_framework import serializers

from cqrs.serializers import CQRSSerializer, CQRSPolymorphicSerializer
from rea_serializers.serializers import ResourceSerializer

from commercia.products.serializers import CategorySerializer
from .models import *


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


class OfferAspectSerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = OfferAspect


class OfferSerializer(CQRSSerializer):
    categories = CategorySerializer(source='categories', many=True)
    resource_contracts = OfferResourceContractSerializer(many=True)
    offer_aspects = OfferAspectSerializer(many=True)

    class Meta:
        model = Offer
        fields = (
            'id',
            'title',
            'categories',
            'short_title',
            'offer_aspects',
            'resource_contracts',
        )
