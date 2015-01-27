import factory

from django.contrib.webdesign import lorem_ipsum


class AgentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = 'rea.Agent'

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(2, common=False).title())


class PlatformFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'platforms.Platform'

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(1, common=False).title())


class QuoteFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'quotes.Quote'

    platform = factory.SubFactory(PlatformFactory)
    recieving_agent = factory.SubFactory(AgentFactory)
    providing_agent = factory.SubFactory(AgentFactory)


class QuoteItemFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'quotes.QuoteItem'

    quote = factory.SubFactory(QuoteFactory)
    offer = factory.SubFactory('offers.factories.OfferFactory')
