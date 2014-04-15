from .models import *

from cqrs.mongo import mongodb
from cqrs.collections import DRFPolymorphicDocumentCollection


class ProductDocumentCollection(DRFPolymorphicDocumentCollection):

    name = 'product'
    model = Product
    serializer_class = 'commercia.products.serializers.ProductSerializer'
    name = 'economica__products'


mongodb.register(ProductDocumentCollection())
