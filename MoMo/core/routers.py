from core import models

class Router():
    '''
    Base class for MoMo routers. Include desired router in perform_create hooks
    of the Payment API view
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

