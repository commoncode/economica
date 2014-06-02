from rest_framework import serializers

from cqrs.serializers import CQRSSerializer
from commercia.offers.serializers import OfferSerializer

from .models import Quote, QuoteItem


class QuoteItemSerializer(CQRSSerializer):
    offer = OfferSerializer()

    class Meta:
        model = QuoteItem


class QuoteSerializer(CQRSSerializer):
    items = QuoteItemSerializer(many=True)
    subtotal = serializers.FloatField(source='calculate_subtotal',
        read_only=True)
    shipping = serializers.FloatField(source='calculate_shipping',
        read_only=True)
    total = serializers.FloatField(source='calculate_total',
        read_only=True)

    class Meta:
        model = Quote
        exclude = 'created_at', 'created_by', 'modified_at', 'modified_by'
