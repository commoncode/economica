from .models import *

from cqrs.mongo import mongodb, DRFDocumentCollection


class ProductDocumentCollection(DRFDocumentCollection):

    name = 'product'
    model = Product
    serializer_class = 'commercia.products.serializers.ProductSerializer' # Polymorphic
    name = 'economica__products'


class VariantDocumentCollection(DRFDocumentCollection):

    name = 'variant'
    model = Variant
    serializer_class = 'commercia.products.serializers.VariantSerializer'
    name = 'economica__products__variants'


mongodb.register(ProductDocumentCollection())
# mongodb.register(VariantDocumentCollection())