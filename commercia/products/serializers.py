from .models import Product

from cqrs.mongo import CQRSPolymorphicSerializer


class ProductSerializer(CQRSPolymorphicSerializer):
    '''
    Polymorphic serializer for the `Resource` model
    '''
    class Meta:
        model = Product
