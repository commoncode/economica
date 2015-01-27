from django.db import models

from rea.models import Resource


class Coupon(Resource):
    '''
    A Coupon is a Resource of sorts that is exchangeable under pre-determined
    conditions as a sort of neo-currency.

    '''

    code = models.CharField(max_length=512)
