from django.db import models

from entropy.base import CreatedMixin, ModifiedMixin
from cqrs.noconflict import classmaker
from cqrs.models import CQRSModel


class Quote(CQRSModel, CreatedMixin, ModifiedMixin):
    '''
    The Quote model is symmetrical to the common Cart model in the majority
    of Shopping Cart models.  We're employing the Quote nomenclature to
    free ourselves from the Product in Cart metaphor which has ultimately
    proved limiting in expression of more sophisticated economic patterns.

    The Quote model has one or more related Quote Line Items of which contain
    an instantiated Contract under Offer on the given Platform which is further
    parameterised with Offer Conditions which influence the nature of the Offer.

    OR

    The Quote model has one or more related Quote Line Items of which contain an
    instantiated Contract Offer or Related Contract Offer...

    '''
    __metaclass__ = classmaker()

    # created_at
    # created_by

    # modified_at
    # modified_by

    platform = models.ForeignKey('platforms.Platform')

    recieving_agent = models.ForeignKey(
        'rea.Agent',
        related_name='%(app_label)s_%(class)s_receiving_agents')

    providing_agent = models.ForeignKey(
        'rea.Agent',
        related_name='%(app_label)s_%(class)s_providing_agents')


    def total(self):
        '''
        Recurse through the QuoteItems and Offers to tally
        the cost from Offer.cost
        '''
        return 0

         


class QuoteItem(CQRSModel):
    '''
    Quote (line) Item

    '''

    quote = models.ForeignKey(
        Quote,
        related_name='items')

    offer = models.ForeignKey(
        'offers.Offer')

    @property
    def resource_contracts(self):
        return self.offer.resource_contracts
