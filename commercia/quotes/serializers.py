from .models import Quote, QuoteItem

from cqrs.serializers import CQRSSerializer


class QuoteItemSerializer(CQRSSerializer):
    class Meta:
        model = QuoteItem


class QuoteSerializer(CQRSSerializer):
    items = QuoteItemSerializer(many=True)

    class Meta:
        model = Quote
