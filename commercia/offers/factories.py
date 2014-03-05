import datetime
import factory
import random

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

    offer = factory.SubFactory(OfferFactory)

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(2, common=False).title())

    chain_evaluation = factory.LazyAttribute(
        lambda o: not not random.randrange(0, 2))

    stop_evaluating = factory.LazyAttribute(
        lambda o: not not random.randrange(0, 2))

    override_evaluation = factory.LazyAttribute(
        lambda o: not not random.randrange(0, 2))


class OfferDiscountFactory(OfferAspectFactory):
    FACTORY_FOR = 'offers.OfferDiscount'

    offer_discount = factory.LazyAttribute(
        lambda o: random.randrange(0, 101))

    offer_discount_is_percentage = factory.LazyAttribute(
        lambda o: not not random.randrange(0, 2))


class OfferNForOneFactory(OfferAspectFactory):
    FACTORY_FOR = 'offers.OfferNForOne'

    title = factory.LazyAttribute(
        lambda o: "%s for one" % this.offer_quantity)

    offer_quantity = random.randrange(0, 5)



