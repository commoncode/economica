from django.db import models
from django.utils.functional import cached_property

from cqrs.noconflict import classmaker
from cqrs.models import CQRSPolymorphicModel, CQRSModel
from entropy.base import (
    EnabledMixin, OrderingMixin, SlugMixin, TitleMixin, StartEndMixin,
    TextMixin
)
from entropy.fields import PriceField
from images.mixins import ImageMixin


#
# Collections
#
class Collection(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    '''
    An arbitrary Collection of Offers according to Promotional themes.
    '''

    def __unicode__(self):
        return self.title


#
# Offers
#
class Offer(CQRSModel, EnabledMixin, StartEndMixin, SlugMixin, TitleMixin,
            ImageMixin):
    '''
    An Offer is an instantiation of a Contract for a Resource as Products or
    Services upon a given Platform.

    An Offer may change according to conditions or rules.

    An Offer may be superseeded by one or more other Related Offers which
    may or may not cumulate.

    We find Offers where we have been used to finding (a catalogue of)
    Products.

    Really, what we're dealing with here is an Offer of a Contract to be
    realised under the Contract Clauses and in combination with the Offer
    Conditions that determine things like Price (under discount or not) or a
    Product offered under a Sales Order or Subscriptions.

    The use of Offers opens the door to create binding Contracts, enforceable
    by Workflow or Finite State Machines for Goods & Services offered under
    any crazy business model that the Enterprise Agent can imagine.

    OR

    An Offer has one or more Offer Conditions, which may or may not cumulate

    ## Attributes

    `contracts`
        A combination of one or more Contracts offering Resources under the
        Conditions specified by the Contract Clauses.

        In this way we can effect concepts such as Bundling with a great deal
        of flexibility for example:

                Product A is offered under a typical RRP SalesOrder contract,
                and combined in the Offer with Product B, offered under a
                Subscription Contract.

                The product text might look like:
                    + Purchase Product A one time, and recieve the associated
                    refil Product B under a 12 Month Subscription.

    `platforms`
        The Platforms aka sales channels underwhich the Contract or Contracts
        mix are Offered. In this way, Offers are reuseable.

    '''
    __metaclass__ = classmaker()

    # enabled
    # start
    # end (optional)

    collections = models.ManyToManyField('Collection', related_name='offers')
    # platforms = models.ManyToManyField('platforms.Platform')

    def __unicode__(self):
        return self.title

    # Offer Aspects
    @cached_property
    def quantity(self):
        quantity = 0

        for aspect in self.offer_aspects.all():
            if (isinstance(aspect, OfferNForOne)):
                quantity = aspect.offer_quantity

                # XXX Can offers have more than one quantity???
                break

        return quantity

    @cached_property
    def price(self):
        price = 0

        for aspect in self.offer_aspects.all():
            if (isinstance(aspect, OfferPrice)):
                price = aspect.offer_price

                # XXX Can offers have more than one price???
                break

        return price

    @cached_property
    def discount(self):
        discount = 0

        for aspect in self.offer_aspects.all():
            if (isinstance(aspect, OfferDiscount)):
                discount = aspect.offer_discount

                # XXX Can offers have more than one discount???
                break

        return discount

    # Images
    @cached_property
    def images(self):
        images = super(Offer, self).images

        if images:
            return images

        try:
            return self.resource_contracts.first().resource.images
        except AttributeError:
            return []

    @cached_property
    def image(self):
        image = super(Offer, self).image

        if image:
            return image

        try:
            return self.resource_contracts.first().resource.image
        except AttributeError:
            return None


class OfferResourceContract(CQRSModel):
    '''
    Conjunct the Contract under which the Resource is Offered, e.g.:

        1 Book under SalesOrder
        2 Bookmarks under SalesOrder
        1 Cosmetic under Autoship (params)

    The related parent Offer class is empty and invalid unless
    it has at least one Resource under Offer of a binding Contract.

    The Offer model then allows combining of Resource Contracts
    to support the concept of Product Bundling
    '''

    offer = models.ForeignKey('Offer', related_name='resource_contracts')
    contract = models.ForeignKey(
        'rea.Contract', related_name='resource_contracts'
    )
    resource = models.ForeignKey(
        'OfferResource', related_name='resource_contracts'
    )

    quantity = models.FloatField()

    def __unicode__(self):
        return '{} of {} under {}'.format(
            self.quantity, self.resource, self.contract
        )


class OfferAspect(CQRSPolymorphicModel, TextMixin, EnabledMixin, OrderingMixin,
                  TitleMixin):
    '''
    Each Offer must specify one or more Aspect Conditions in which the
    Contract Offer might be valid.

    This can include altering the Price and circumstances of the Contract.

    The Contract under Offer expects to be influenced by the conditions that
    it is Offered under. When the Contract is finally instantiated as an
    Actual Contract, the Conditions in which it were offered under play a part
    in determining its Clauses and Parameters.

    ## Attributes:

    `offer`
        the offer that this aspect should affect

    `chain_evaluation`
        offer aspects can be combined to create unique Promotion Offers of any
        type. The chain is broken when there is a sequence discontinuation is
        `chain_evaluation = True`

    `override_evaluation`
        the Offer Aspect or Offer Aspect Chain overrides all previous

    '''

    # title
    # short_title
    # description
    # order
    # enabled

    offer = models.ForeignKey('Offer', related_name='offer_aspects')

    # evaluate in combination with previous others / evaluate separately
    chain_evaluation = models.BooleanField(default=None)

    # stop evaluating all other aspects beyond this one.
    stop_evaluating = models.BooleanField(default=None)

    # override all previous offer aspect chains
    override_evaluation = models.BooleanField(default=None)


class OfferPrice(OfferAspect):
    '''
    Offer Price for the given Contract

    Assumes the Exhange Resource is Cash?
    '''
    # Need to confirm the best field type for prices.
    offer_price = models.FloatField(blank=True)


class OfferResource(OfferAspect):
    '''
    Optionally specify other Resource to satisfy the exchange,
    e.g. One Pig for 4 Chickens
    '''
    resource = models.ForeignKey('rea.Resource')
    quantity = models.FloatField()


class OfferDiscount(OfferAspect):
    '''
    Offer a Discount in the form of a Percentage or Deduction
    '''
    offer_discount = models.FloatField()
    offer_discount_is_percentage = models.BooleanField(default=True)


class OfferValidUntil(OfferAspect, StartEndMixin):
    '''
    Here we add a Validity period for an Aspect Condition of the Offer.

    This Aspect might be used to create a Flash Sale for the parent Offer
    '''

    # start
    # end (optional)
    pass


class OfferStart(OfferAspect):
    pass


class OfferEnd(OfferAspect):
    pass


class OfferRelated(OfferAspect):
    '''
    Here we might add Related Offers to the Primary Offer.  This might take
    the form of Offering a closely Related Product to accompany the Primary
    Offer.

    Setting the `related_contract_price` to zero or the
    `related_contract_discount` to 100% results in a Free Gift
    '''

    related_offer = models.ForeignKey(
        'Offer', related_name='%(app_label)s_%(class)s_related_offer'
    )
    related_contract_price = models.FloatField()
    related_contract_discount = models.FloatField()


class OfferFreeGift(OfferAspect):
    '''
    The existence of this Offer Aspect enables the combining with another Offer
    for Free
    '''
    free_offer = models.ForeignKey(
        'Offer',
        related_name='%(app_label)s_%(class)s_free_offer')

    def __unicode__(self):
        return '{} of {} under {}'.format(
            self.quantity, self.resource, self.contract
        )


class OfferFreeShipping(OfferAspect):
    '''
    Offer Free Shipping

    def __unicode__(self):
        return '%s of %s under %s' % (
            self.quantity,
            self.resource,
            self.contract
        )
    '''
    offer_free_shipping = models.BooleanField(default=None)


class OfferNForOne(OfferAspect):
    '''
    Offer a quantity of the same Contract for the same Product with Product
    Variants.
    '''

    offer_quantity = models.IntegerField()  # 2 or more

    # apply_to = ['category', 'product', 'variant',]  default 'product'

    '''
    XXX strategy to offer 'like' Products, i.e. offering Product Variants of
    the same Product. Or open up to Products within the same Category, i.e.
    't-shirts' validate on save offer_quantity
    '''


class OfferToAgent(OfferAspect):
    '''
    Theoretically offer a unique set of Agents an Offer Aspect based
    on some kind of activity.

    For example, if the Agent has had this Offer or a Related Offer
    in their Quote/Cart before then perhaps offer them a better deal?

    Note: these are best created with an algorithm.  Rule-based
    Offer Aspects will be better applicable.

    Combine this with other Offer Aspects such as:

        OfferDiscount
        OfferValidUntil

    To give limited time offers based on

    '''

    agents = models.ManyToManyField('rea.Agent')

    reason = models.TextField()


class OfferCoupon(OfferAspect):
    '''
    Coupons Rules

    The Offer is redeemable against a Coupon.  What is a Coupon?

    Coupons are a Resource that can be exchanged under certain
    bound Contractual Conditions.

    '''
    # XXX Coupons have rules. Add them to determine validity.
    # XXX relate to a Contract for now.
    coupon = models.ForeignKey('coupons.Coupon')


class OfferOnQuote(OfferAspect):
    '''
    Watch the quote for given conditions and provide an
    Offer.  Such as OfferFreeGift.
    '''
    minimum = PriceField()
