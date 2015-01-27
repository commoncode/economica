from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Quote
from .serializers import QuoteSerializer


class QuoteDocumentCollection(DRFDocumentCollection):
    model = Quote
    serializer_class = QuoteSerializer
    name = 'economica__quotes'


mongodb.register(QuoteDocumentCollection())
