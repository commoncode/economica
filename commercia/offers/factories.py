import datetime
import factory

from django.contrib.webdesign import lorem_ipsum

from faker import Factory


fake = Factory.create()


class ContractFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = 'rea.Contract'

	# resource
	# agent


class OfferFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'offers.Offer'

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(5, common=False).title())

    start = factory.LazyAttribute(
    	lambda o: datetime.datetime.now())

    enabled = True


    # @factory.post_generation
    # def contracts(self, create, extracted, **kwargs):
    #     if not create:
    #         # Simple build, do nothing.
    #         return

    #     if extracted:
    #         # A list of contracts were passed in, use them
    #         for contract in extracted:
    #             self.contracts.add(contract)

    
class OfferAspectFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'offers.OfferAspect'

