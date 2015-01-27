from django.db import models


class Promotion(models.Model):
    """
    A Promotion is a dissemination of information about a Product or Service
    and a series of related Offers for those Resources.

    A Promotion in Economica is essentially a reuseable, stored set of
    Promotional rules and content which affect Offers of Product by creating
    new Offers or adding OfferAspects to existing Offers.

    An example of a Promotion that adds OfferAspects might be '50% of
    everything in-store', which, for the validity time of the Promotion, as
    determined by its governing Campaign, adds a OfferDiscount to every Offer
    found on the Store Platform which is populated with the discount amount of
    0.50

    To run a Promotion, it must be instantiated in a Campaign, which
    coordinates the timing of Promotional events; allowing Promotions to be
    sequenced, repeated, or otherwise completely coordinated well in advance.

    """

    # title
    # short_title
    # enabled
