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

    `contracts`
        A combination of one or more Contracts offering Resources under the Conditions
        specified by the Contract Clauses.

        In this way we can effect concepts such as Bundling with a great deal of flexibility
        for example:

                Product A is offered under a typical RRP SalesOrder contract, and combined in the Offer
                with Product B, offered under a Subscription Contract.

                The product text might look like:

                    + Purchase Product A one time, and recieve the associated refil Product B under a
                    12 Month Subscription.

    `platforms`
        The Platforms aka sales channels underwhich the Contract or Contracts mix are Offered.  In this
        way, Offers are reuseable.

    """

    # start
    # end (optional)
    # enabled

    contracts = models.ManyToManyField('rea.Contract')

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

    ## Attributes:

    `offer`
        the offer that this aspect should affect

    `chain_evaluation`
        offer aspects can be combined to create unique Promotion Offers of any type.  The
        chain is broken when there is a sequence discontinuation is `chain_evaluation = True`

    `override_evaluation`
        the Offer Aspect or Offer Aspect Chain overrides all previous

    """

    # title
    # short_title
    # description
    # order
    # enabled

    offer = models.ForeignKey('Offer')

    chain_evaluation = models.BooleanField()  # evaluate in combination with previous others / evaluate separately
    stop_evaluating = models.BooleanField()  # stop evaluating all other aspects beyond this one.
    override_evaluation = models.BooleanField()  # override all previous offer aspect chains


class OfferPrice(OfferAspect):
    """
    Offer Price for the given Contract
    """
    offer_price = models.FloatField(blank=True)  # Need to confirm the best field type for prices.


class OfferDiscount(OfferAspect):
    """
    Offer a Discount in the form of a Percentage or Deduction
    """
    offer_discount = models.FloatField()
    offer_discount_is_percentage = models.BooleanField(default=True)


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

    Setting the `related_contract_price` to zero or the `related_contract_discount` to 100%
    results in a Free Gift
    """

    related_offer = models.ForeignKey(
        'Offer',
        related_name="%(app_label)s_%(class)s_related_offer")
    related_contract_price = models.FloatField()
    related_contract_discount = models.FloatField()


class OfferFreeGift(OfferAspect):
    """
    The existence of this Offer Aspect enables the combining with another Offer
    for Free
    """
    free_offer = models.ForeignKey(
        'Offer',
        related_name="%(app_label)s_%(class)s_free_offer")


class OfferFreeShipping(OfferAspect):
    """
    Offer Free Shipping
    """
    offer_free_shipping = models.BooleanField()


class OfferNForOne(OfferAspect):
    """
    Offer a quantity of the same Contract for the same Product with Product Variants.

    """

    offer_quantity = models.IntegerField()  # 2 or more

    # apply_to = ['category', 'product', 'variant',]  default 'product'

    # XXX strategy to offer 'like' Products, i.e. offering Product Variants of the same Product.  Or
    # open up to Products within the same Category, i.e. 't-shirts'
    # validate on save offer_quantity


class OfferIndividualAgent(OfferAspect):
    """
    Theoretically offer a unique set of Agents an Offer Aspect based on some kind of
    activity.

    For example, if the Agent has had this Offer or a Related Offer in their Quote/Cart before
    then perhaps offer them a better deal?

    Note: these are best created with an algorithm.  Rule-based Offer Aspects will be better applicable.

    """

    agents = models.ManyToManyField('rea.Agent')

