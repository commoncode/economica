from faker import Factory

fake = Factory.create()


class QuoteFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'quotes.Quote'

    #platform
    #recieving_agent
    #providing_agent

    @factory.post_generation
    def quote_items(self, create, extracted, **kwargs):
        pass


class QuoteItemFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'quotes.QuoteItem'

    offer = factory.SubFactory('commercia.offers.factories.OfferFactory')
