from .models import Quote, QuoteItem

from cqrs.serializers import CQRSSerializer
from commercia.offers.serializers import OfferSerializer


class QuoteItemSerializer(CQRSSerializer):

    offer = OfferSerializer()    

    class Meta:
        model = QuoteItem


class QuoteSerializer(CQRSSerializer):

    items = QuoteItemSerializer(many=True)

    class Meta:
        model = Quote


