import datetime
import factory
import random

from django.contrib.webdesign import lorem_ipsum
from django.template.defaultfilters import slugify

from fakers import lipservice

from faker import Factory


fake = Factory.create()


class OfferFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'offers.Offer'

    title = factory.LazyAttribute(
        lambda o: lipservice.words(3, common=False).title())

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
        lambda o: lipservice.words(2, common=False).title())

    chain_evaluation = factory.LazyAttribute(
        lambda o: not not random.randrange(0, 2))

    stop_evaluating = factory.LazyAttribute(
        lambda o: not not random.randrange(0, 2))

    override_evaluation = factory.LazyAttribute(
        lambda o: not not random.randrange(0, 2))


class OfferPriceFactory(OfferAspectFactory):
    FACTORY_FOR = 'offers.OfferPrice'

    offer_price = factory.LazyAttribute(
        lambda o: round(random.random() * 100, 2))


class OfferResourceFactory(OfferAspectFactory):
    FACTORY_FOR = 'offers.OfferResource'

    resource = factory.SubFactory('products.Product')
    quantity = factory.LazyAttribute(
        lambda o: random.randrange(0, 100))


class OfferDiscountFactory(OfferAspectFactory):
    FACTORY_FOR = 'offers.OfferDiscount'

    offer_discount = factory.LazyAttribute(
        lambda o: random.randrange(0, 101))

    offer_discount_is_percentage = factory.LazyAttribute(
        lambda o: not not random.randrange(0, 2))


class OfferNForOneFactory(OfferAspectFactory):
    FACTORY_FOR = 'offers.OfferNForOne'

    offer_quantity = factory.LazyAttribute(
        lambda o: random.randrange(1, 10))

    @factory.post_generation
    def create_title(self, create, extracted, **kwargs):
        self.title = "%s for one" % self.offer_quantity
        self.save()


class OfferToAgentsFactory(OfferAspectFactory):
    FACTORY_FOR = 'offers.OfferToAgent'


#
# Collections
#
class CollectionFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'offers.Collection'

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(3, common=False).title())
    slug = factory.LazyAttribute(
        lambda o: slugify(lorem_ipsum.words(5, common=False)))
