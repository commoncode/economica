from .models import *

from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection


class OfferDocumentCollection(DRFDocumentCollection):

    name = 'offer'
    model = Offer
    serializer_class = 'commercia.offers.serializers.OfferSerializer'
    name = 'economica__offers'


mongodb.register(OfferDocumentCollection())
