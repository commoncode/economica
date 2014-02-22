import datetime
import factory

from django.contrib.webdesign import lorem_ipsum

from faker import Factory


fake = Factory.create()


class ProductFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'products.Product'

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(5, common=False).title())

    @factory.post_generation
    def variants(self, create, extracted, **kwargs):

        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of contracts were passed in, use them
            for contract in extracted:
                self.contracts.add(contract)


class VariantFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'products.Variant'

    product = factory.SubFactory(ProductFactory)