from rest_framework import serializers

from cqrs.mongo import CQRSSerializer, CQRSPolymorphicSerializer
from rea_serializers.serializers import ResourceSerializer

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
    '''
    Serializer for Polymorphic Model OfferAspect.
    '''

    class Meta:
        model = OfferAspect


class OfferSerializer(CQRSSerializer):
    '''
    Serializer for the `SubscriptionContract` model
    '''

    resource_contracts = OfferResourceContractSerializer(many=True)
    offer_aspects = OfferAspectSerializer(many=True)

    class Meta:
        model = Offer
        fields = (
            'id', 
            'title',
            'short_title',
            'offer_aspects',
            'resource_contracts',
        )


