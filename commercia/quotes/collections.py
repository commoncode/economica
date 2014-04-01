from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Quote, QuoteItem


class QuoteDocumentCollection(DRFDocumentCollection):
    name = 'quote'
    model = Quote
    serializer_class = 'commercia.quotes.serializers.QuoteSerializer'
    name = 'economica__quotes'


mongodb.register(QuoteDocumentCollection())
