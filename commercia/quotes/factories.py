import factory

from faker import Factory


fake = Factory.create()


class QuoteFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'quotes.Quote'

    platform_id = 1
    recieving_agent_id = 1
    providing_agent_id = 1


class QuoteItemFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'quotes.QuoteItem'

    offer = factory.SubFactory('commercia.offers.factories.OfferFactory')
