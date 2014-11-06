from django.db import models
from django.utils.functional import cached_property

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
    parameterised with Offer Conditions which influence the nature of the
    Offer.

    OR

    The Quote model has one or more related Quote Line Items of which contain
    an instantiated Contract Offer or Related Contract Offer...

    '''
    __metaclass__ = classmaker()

    # created_at
    # created_by

    # modified_at
    # modified_by

    # platform = models.ForeignKey('platforms.Platform')
    recieving_agent = models.ForeignKey(
        'rea.Agent', null=True,
        related_name='%(app_label)s_%(class)s_receiving_agents'
    )
    providing_agent = models.ForeignKey(
        'rea.Agent', related_name='%(app_label)s_%(class)s_providing_agents'
    )

    @cached_property
    def calculate_subtotal(self):
        return self.items.aggregate(models.Sum('total'))['total__sum'] or 0

    @cached_property
    def calculate_shipping(self):
        # How are we gonna calculate shipping?
        return 15

    @cached_property
    def calculate_total(self):
        # On a method for VIP changes maybe?
        return self.calculate_subtotal + self.calculate_shipping


class QuoteItem(CQRSModel):
    '''
    Quote (line) Item

    '''

    quote = models.ForeignKey(Quote, related_name='items')
    offer = models.ForeignKey('offers.Offer')
    quantity = models.PositiveIntegerField(default=1)
    total = models.FloatField(default=0)

    class Meta:
        unique_together = ('quote', 'offer')

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.offer.price
        super(QuoteItem, self).save(*args, **kwargs)

    @cached_property
    def resource_contracts(self):
        return self.offer.resource_contracts
