from django.db import models


class Campaign(models.Model):
    """
    Campaign, which coordinates the timing
    of Promotional events; allowing Promotions to be sequenced, repeated,
    or otherwise completely coordinated well in advance.

    """

    # title
    # short_title
    # enabled
    pass


class CampaignPromotion(models.Model):
    """
    Instantiate a Promotion for this Campaign

    """

    # start
    # end (optional)
    # enabled

    promotion = models.ForeignKey('promotions.Promotion')

    # XXX Validate against Overlapping Promotions?
