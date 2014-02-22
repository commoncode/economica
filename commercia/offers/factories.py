import datetime
import factory

from django.contrib.webdesign import lorem_ipsum

from faker import Factory


fake = Factory.create()


class OfferFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'offers.Offer'

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(5, common=False).title())

    start = factory.LazyAttribute(
        lambda o: datetime.datetime.now())

    enabled = True


    @factory.post_generation
    def resource_contracts(self, create, extracted, **kwargs):
    
        if not create:
            # Simple build, do nothing.
            return

        OfferResourceContractFactory(offer=self) 

        if extracted:
            # A list of contracts were passed in, use them
            for resource_contract in extracted:
                self.resource_contracts.add(resource_contract)

    
class OfferResourceContractFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'offers.OfferResourceContract'

    offer = factory.SubFactory(OfferFactory)
    contract = factory.SubFactory('rea_patterns_b2c.patterns.salesorder.factories.SalesOrderFactory')
    resource = factory.SubFactory('commercia.products.factories.ProductFactory')
    quantity = 1


class OfferAspectFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'offers.OfferAspect'
