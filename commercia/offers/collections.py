from .models import Offer, OfferAspect

from cqrs.mongo import mongodb, DRFDocumentCollection


class OfferDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Contract`
    """
    name = 'offer'
    model = Offer
    serializer_class = 'commercia.offers.serializers.OfferSerializer'
    name = 'economica__offers'


mongodb.register(OfferDocumentCollection())
