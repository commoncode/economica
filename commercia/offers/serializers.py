from cqrs.mongo import CQRSSerializer

from .models import Offer


class OfferSerializer(CQRSSerializer):
    """
    Serializer for the `SubscriptionContract` model
    """

    # aspects = OfferAspectSerializer()

    class Meta:
        model = Offer
        fields = (
            "id", "title", "short_title"
        )


class OfferAspectSerializer(CQRSSerializer):
    """
    Serializer for Polymorphic Model OfferAspect.
    """

    class Meta:
        model = 'offers.OfferAspect'

        # dynamically add fields according to the downcast
        fields = (
            "id", "title", "short_title"
        )
