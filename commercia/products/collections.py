from .models import *

from cqrs.mongo import mongodb, DRFDocumentCollection


class ProductDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Products`
    """
    name = 'product'
    model = Product
    serializer_class = 'commercia.products.serializers.ProductSerializer' # Polymorphic
    name = 'economica__products'

    # XXX add signal listeners to models downcast from Product.

mongodb.register(ProductDocumentCollection())