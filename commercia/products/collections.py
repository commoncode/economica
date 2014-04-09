from cqrs.mongo import mongodb
from cqrs.collections import DRFPolymorphicDocumentCollection

from .models import Product
from .serializers import ProductSerializer


class ProductDocumentCollection(DRFPolymorphicDocumentCollection):
    model = Product
    serializer_class = ProductSerializer
    name = 'economica__products'


mongodb.register(ProductDocumentCollection())
