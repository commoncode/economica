from cqrs.mongo import CQRSSerializer

from rest_framework import serializers

from .models import *


class OfferResourceContractSerializer(CQRSSerializer):

    class Meta:
        model = OfferResourceContract
        fields = (
            'id', 
            'contract', 
            'resource', 
            'quantity'
        )

# XXX Dynamically create these classes passingin the Model at
# runtime: http://stackoverflow.com/questions/15247075/how-can-i-dynamically-create-derived-classes-from-a-base-class

class OfferDiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfferDiscount


class OfferNForOneSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfferNForOne


class OfferAspectSerializer(CQRSSerializer):
    '''
    Serializer for Polymorphic Model OfferAspect.
    '''

    class Meta:
        model = OfferAspect

    def to_native(self, obj):
        """
        Because OfferAspect is Polymorphic
        """


        if isinstance(obj, OfferDiscount):
            return OfferDiscountSerializer(obj).to_native(obj)

        if isinstance(obj, OfferNForOne):
            return OfferNForOneSerializer(obj).to_native(obj)
        return super(OfferAspectSerializer, self).to_native(obj)


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
            'resource_contracts'
        )


