from .models import (
    Offer, OfferAspect, OfferResourceContract
)

from cqrs.mongo import mongodb, DRFDocumentCollection


class OfferDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Offers`
    """
    name = 'offer'
    model = Offer
    serializer_class = 'commercia.offers.serializers.OfferSerializer'
    name = 'economica__offers'


class OfferResourceContractDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Offers`
    """
    name = 'offerresourcecontract'
    model = OfferResourceContract
    serializer_class = 'commercia.offers.serializers.OfferResourceContractSerializer'
    parent_collection = OfferDocumentCollection
    name = 'economica__offers__resourcecontracts'


class OfferAspectDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Offer Aspects`
    """
    name = 'offeraspect'
    model = OfferAspect
    serializer_class = 'commercia.offers.serializers.OfferAspectSerializer'
    name = 'economica__offers__offeraspects'


mongodb.register(OfferDocumentCollection())
mongodb.register(OfferResourceContractDocumentCollection())
mongodb.register(OfferAspectDocumentCollection())
