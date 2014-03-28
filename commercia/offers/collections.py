from .models import *

from cqrs.mongo import mongodb, DRFDocumentCollection


class OfferDocumentCollection(DRFDocumentCollection):

    name = 'offer'
    model = Offer
    serializer_class = 'commercia.offers.serializers.OfferSerializer'
    name = 'economica__offers'


class OfferResourceContractDocumentCollection(DRFDocumentCollection):

    name = 'offerresourcecontract'
    model = OfferResourceContract
    serializer_class = 'commercia.offers.serializers.OfferResourceContractSerializer'
    # parent_collection = OfferDocumentCollection
    name = 'economica__offers__resourcecontracts'


class OfferAspectDocumentCollection(DRFDocumentCollection):

    name = 'offeraspect'
    model = OfferAspect
    serializer_class = 'commercia.offers.serializers.OfferAspectSerializer'
    name = 'economica__offers__offeraspects'


mongodb.register(OfferDocumentCollection())
mongodb.register(OfferResourceContractDocumentCollection())
mongodb.register(OfferAspectDocumentCollection())
