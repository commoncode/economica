from django.db import models

from cqrs.models import CQRSPolymorphicModel
from entropy.base import SlugMixin, TitleMixin


# Create your models here.
class AspectQuality(CQRSPolymorphicModel, SlugMixin, TitleMixin):
    # title
    # slug

    pass


class Color(AspectQuality):
    hex = models.CharField(max_length='6')

    '''
    def hsv(self):
        return h, s, v

    def rgb(self):
        return r, g, b

    def hsl(self):
        return h, s, l

    def name
        determine the name from some kinda color chart
    '''


class Size(AspectQuality):
    # title
    # short_title
    # slug

    dimension = models.CharField(max_length=512)
    measure = models.CharField(max_length=128)


class Property(AspectQuality):
    # title
    # short_title
    # slug

    value = models.CharField(max_length=256)
