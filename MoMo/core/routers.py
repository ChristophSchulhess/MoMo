'''
Payment data routers. To be included in perform_create hook of the PaymentList
APIView.
'''
import requests
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
        dest = models.SaasInstance.objects.get(id=data['account_id'])
        return requests.post(dest.url, data).raise_for_status()

class ReferenceIdRouter(Router):
    '''
    The ReferenceIdRouter has to retrieve customer identifiers from the known
    SaaS instances since this information will likely be located in their
    domain. As soon as an instance sends a confirmation, it will dispatch the
    payment data to that instance (We assume that instances provide some kind of
    API to retrieve the required information).
    '''
    def route(self, data):
        saas_instances = models.SaasInstance.objects.all()
        dest = None
        for instance in saas_instances:
            # This call depends on the instance API
            response = requests.get('{}/{}/'.format(instance.url,
                data['reference_id']))
            # Some way of verifying confirmation, depends on API as well
            if response.status_code == 200 and len(response.json()) == 1:
                dest = instance
                break
        if not dest:
            return False
        return requests.post(dest.url, data).raise_for_status()


