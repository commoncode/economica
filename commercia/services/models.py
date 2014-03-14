from django.db import models

# Create your models here.


class Service(Resource):
	'''
	Offer a service to be performed by an Agent.  The Contract defines
	whom the providing_agent is. The ContractInstance defines the 
	recieving_agent.

	'''
	pass


class Consult(Service):
	'''
	Consulting as a Service probably offered under an hourly rate.
	
	'''
	pass