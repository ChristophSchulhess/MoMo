'''
Payment data routers. To be included in perform_create hook of the PaymentList
APIView.
'''
from core import models

class Router():
    '''
    Base class for MoMo routers.
    '''
    def __init__(self):
        pass

    def route(self, data):
        pass

class AccountIdRouter(Router):
    '''
    The AccountIdRouter will retrieve the url of the SaaS instance that
    corresponds to the account_id field of a given payment and send the payment
    data there.
    '''
    def route(self, data):
        pass

class ReferenceIdRouter(Router):
    '''
    The ReferenceIdRouter has to retrieve customer identifiers from the known
    SaaS instances since this information will likely be located in their
    domain. As soon as an instance sends a confirmation, it will dispatch the
    payment data to that instance.
    '''
    def route(self, data):
        pass

