from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Collection, Offer, OfferResourceContract
from .serializers import (
    CollectionSerializer, OfferResourceContractSerializer, OfferSerializer
)


class CollectionDocumentCollection(DRFDocumentCollection):
    model = Collection
    serializer_class = CollectionSerializer
    name = 'economica__collections'


class OfferResourceContractDocumentCollection(DRFDocumentCollection):
    model = OfferResourceContract
    serializer_class = OfferResourceContractSerializer
    name = 'economica__resource_contracts'


class OfferDocumentCollection(DRFDocumentCollection):
    model = Offer
    serializer_class = OfferSerializer
    name = 'economica__offers'


mongodb.register(CollectionDocumentCollection())
mongodb.register(OfferResourceContractDocumentCollection())
mongodb.register(OfferDocumentCollection())
