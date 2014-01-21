from entropy.models import \
    DescriptionMixin, \
    EnabledMixin, \
    OrderingMixin, \
    StartEndMixin, \
    TitleMixin


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
    Workflow or Finite State Machine for Goods & Services offered under any crazy
    business model that the Enterprise Agent can imagine.

    OR

    An Offer has one or more Offer Conditions, which may or may not cumulate

    """

    # start
    # end (optional)
    # enabled

    contract = models.ForeignKey('rea.contracts.Contract')

    platforms = models.ManyToManyField('platform.Platform')


class RelatedOffer(PolyMorphicModel):
    """
    A Related Offer is a sub offer placed atop of a Primary Offer.

    A Related Offer can be offered in conjunction with a Primary Offer or as a Replacement

    """

    offer = models.ForeignKey('Offer')


class OfferCondition(DescriptionMixin, EnabledMixin, OrderingMixin, StartEndMixin, TitleMixin):
    """
    Each Offer must specify one or more Conditions in which the Contract Offer
    might be valid.

    This can include altering the Price and circumstances of the Contract.

    The Contract under Offer expects to be influenced by the conditions that it is
    Offered under.  When the Contract is finally instantiated as an Actual Contract,
    The Conditions in which it were offered under play a part in determining its Clauses
    and Parameters.
    """
    # title
    # short_title
    # description
    # order
    # start
    # end (optional)
    # enabled

    offer = models.ForeignKey('Offer')


    contract_price = models.FloatField()  # Need to confirm the best field type for prices.
    contract_discount = models.FloatField()



