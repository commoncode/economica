from cqrs.mongo import mongodb
from cqrs.collections import (
    DRFDocumentCollection,
    DRFPolymorphicDocumentCollection
)

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryDocumentCollection(DRFDocumentCollection):
    model = Category
    serializer_class = CategorySerializer
    name = 'economica__categories'


class ProductDocumentCollection(DRFPolymorphicDocumentCollection):
    model = Product
    serializer_class = ProductSerializer
    name = 'economica__products'


mongodb.register(CategoryDocumentCollection())
mongodb.register(ProductDocumentCollection())
