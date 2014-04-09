from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Offer
from .serializers import OfferSerializer


class OfferDocumentCollection(DRFDocumentCollection):
    model = Offer
    serializer_class = OfferSerializer
    name = 'economica__offers'


mongodb.register(OfferDocumentCollection())
