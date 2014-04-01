from .models import Quote

from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection


class QuoteDocumentCollection(DRFDocumentCollection):

    name = 'quote'
    model = Quote
    serializer_class = 'commercia.quotes.serializers.QuoteSerializer'
    name = 'economica__quotes'


mongodb.register(QuoteDocumentCollection())
