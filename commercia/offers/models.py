from django.db import models

from entropy.base import \
    TextMixin, \
    EnabledMixin, \
    OrderingMixin, \
    StartEndMixin, \
    TitleMixin
from rea.models.core import REAModel


class Offer(EnabledMixin, StartEndMixin):
    """
    An Offer is an instantiation of a Contract for a Resource as Products or
    Services upon a given Platform.

    An Offer may change according to conditions or rules.

    An Offer may be superseeded by one or more other Related Offers which
    may or may not cumulate.

    We find Offers where we have been used to finding (a catalogue of) Products.
    Really, what we're dealing with here is an Offer of a Contract to be realised
    under the Contract Clauses and in combination with the Offer Conditions that
    determine things like Price (under discount or not) or a Product offered under
    a Sales Order or Subscriptions.

    The use of Offers opens the door to create binding Contracts, enforceable by
    Workflow or Finite State Machines for Goods & Services offered under any crazy
    business model that the Enterprise Agent can imagine.

    OR

    An Offer has one or more Offer Conditions, which may or may not cumulate

    ## Attributes



    """

    # start
    # end (optional)
    # enabled

    contract = models.ForeignKey('rea.Contract')

    platforms = models.ManyToManyField('platforms.Platform')


class OfferAspect(REAModel, TextMixin, EnabledMixin, OrderingMixin, TitleMixin):
    """
    Each Offer must specify one or more Aspect Conditions in which the Contract Offer
    might be valid.

    This can include altering the Price and circumstances of the Contract.

    The Contract under Offer expects to be influenced by the conditions that it is
    Offered under.  When the Contract is finally instantiated as an Actual Contract,
    The Conditions in which it were offered under play a part in determining its Clauses
    and Parameters.

    Attributes:

    offer
        fk
    contract_price
        set the price of the contract for this given aspect/offer/platform(s)
    contract_discount
        apply an optional discount
    """
    # title
    # short_title
    # description
    # order
    # enabled

    offer = models.ForeignKey('Offer')

    contract_price = models.FloatField(blank=True)  # Need to confirm the best field type for prices.
    contract_discount = models.FloatField(blank=True)

    accumulate_evaluation = models.BooleanField()
    continue_evaluation = models.BooleanField()



class OfferValidUntil(OfferAspect, StartEndMixin):
    """
    Here we add a Validity period for an Aspect Condition of the Offer.

    This Aspect might be used to create a Flash Sale for the parent Offer
    """
    # start
    # end (optional)
    pass


class OfferRelated(OfferAspect):
    """
    Here we might add Related Offers to the Primary Offer.  This might take the form
    of Offering a closely Related Product to accompany the Primary Offer.

    """
    related_offer = models.ForeignKey(
        'Offer',
        related_name="%(app_label)s_%(class)s_related_offer")
    related_contract_price = models.FloatField()
    related_contract_discount = models.FloatField()


class OfferIndividualAgent(OfferAspect):
    """
    Theoretically offer a unique set of Agents an Offer Aspect based on some kind of
    activity.

    For example, if the Agent has had this Offer or a Related Offer in their Quote/Cart before
    then perhaps offer them a better deal?
    """
    pass
