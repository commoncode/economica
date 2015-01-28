from django.db import models

from cqrs.models import CQRSModel
from entropy.base import EnabledMixin, SlugMixin, TitleMixin


# Create your models here.
class Category(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    # title
    # slug
    # is_enabled

    parent = models.ForeignKey('self', null=True, related_name='children')

    def __unicode__(self):
        return self.title
