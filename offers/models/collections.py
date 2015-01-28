from django.db import models

from cqrs.models import CQRSModel
from entropy.base import EnabledMixin, SlugMixin, TitleMixin


# Create your models here.
class Collection(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    '''
    An arbitrary Collection of Offers according to Promotional themes.
    '''

    class Meta:
        app_label = 'offers'

    def __unicode__(self):
        return self.title


"""
class SmartCollection(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    '''
    A collection of objects according to specified aspect rules.

    Either Products or Offers

    '''

    # title
    # slug
    # is_enabled

    pass


class SmartCollectionAspectInstance(CQRSModel):
    entity = models.ForeignKey('SmartCollection')
    aspect = models.ForeignKey('SmartCollectionAspect')


class SmartCollectionAspectRule(CQRSModel):
    pass


class SmartCollectionAspect(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    # title
    # slug
    # is_enabled

    rules = models.ForeignKey('SmartCollectionAspectRule')
"""
