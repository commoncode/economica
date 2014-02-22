from cqrs.mongo import CQRSSerializer

from rest_framework import serializers

from .models import (
    Offer, OfferAspect, OfferResourceContract
)


class OfferResourceContractSerializer(CQRSSerializer):

    class Meta:
        model = OfferResourceContract
        fields = (
            'id', 
            'contract', 
            'resource', 
            'quantity'
        )


class OfferSerializer(CQRSSerializer):
    '''
    Serializer for the `SubscriptionContract` model
    '''

    resource_contracts = OfferResourceContractSerializer(many=True)

    class Meta:
        model = Offer
        fields = (
            'id', 
            'title', 
            'short_title',
            'resource_contracts'
        )


class OfferAspectSerializer(CQRSSerializer):
    '''
    Serializer for Polymorphic Model OfferAspect.
    '''

    class Meta:
        model = OfferAspect
        # dynamically add fields according to the downcast
        fields = (
            'id', 'title', 'short_title'
        )

