from .models import *

from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection


class ProductDocumentCollection(DRFDocumentCollection):

    name = 'product'
    model = Product
    serializer_class = 'commercia.products.serializers.ProductSerializer'
    name = 'economica__products'


mongodb.register(ProductDocumentCollection())
