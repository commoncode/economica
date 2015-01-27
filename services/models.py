from django.db import models

from rea.models import Resource

# Create your models here.


class Service(Resource, models.Model):
    '''
    Offer a service to be performed by an Agent.  The Contract defines
    whom the providing_agent is. The ContractInstance defines the
    recieving_agent.

    '''
    pass


class Consult(Service, models.Model):
    '''
    Consulting as a Service probably offered under an hourly rate.

    '''
    pass
