from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Collection, Offer
from .serializers import CollectionSerializer, OfferSerializer


class CollectionDocumentCollection(DRFDocumentCollection):
    model = Collection
    serializer_class = CollectionSerializer
    name = 'economica__collections'


class OfferDocumentCollection(DRFDocumentCollection):
    model = Offer
    serializer_class = OfferSerializer
    name = 'economica__offers'


mongodb.register(CollectionDocumentCollection())
mongodb.register(OfferDocumentCollection())
