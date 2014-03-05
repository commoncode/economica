from django.db.models.signals import post_save

from .models import Offer

import zerorpc




def new_offers(sender, **kwargs):
    # Your specific logic here
    # TODO
    # Hook into the Economica DDP service.
    # c = zerorpc.Client()
    # c.connect("tcp://127.0.0.1:4242")
    # c.offers()
    # c.close()
    print ('Offer signal raised')

post_save.connect(new_offers, sender=Offer)	