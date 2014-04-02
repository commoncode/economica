from cqrs.serializers import CQRSSerializer
from commercia.offers.serializers import OfferSerializer

from .models import Quote, QuoteItem


class QuoteItemSerializer(CQRSSerializer):
    offer = OfferSerializer()

    class Meta:
        model = QuoteItem
        fields = (
            'id',
            'quote',
            'offer',
            'quantity'
        )


class QuoteSerializer(CQRSSerializer):
    items = QuoteItemSerializer(many=True)

    class Meta:
        model = Quote
        fields = (
          'id',
          'items',
          'platform',
          'providing_agent',
          'recieving_agent'
        )
