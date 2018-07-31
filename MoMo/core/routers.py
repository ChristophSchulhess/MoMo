'''
Payment data routers. To be included in perform_create hook of the PaymentList
APIView.
'''
import requests
from core import models

class Router():
    '''
    Base class for MoMo routers. A return value (error state) of None refers to
    a succesful transaction.
    '''
    def __init__(self):
        self.dest = None

    def route(self, data):
        '''
        Basic route method to be overwritten by child routers. Simply attempts
        to send the data and returns exceptions if a) a ConnectionError occurs
        (i.e. SaaS instance is down) or b) the HTTP responses status code is an
        error (i.e. 4XX or 5XX). Handling of these cases should be done in
        views.
        '''
        try:
            response = requests.post(self.dest.url, data)
        except ConnectionError as connection_error:
            return connection_error
        return response.raise_for_status()


class AccountIdRouter(Router):
    '''
    The AccountIdRouter will retrieve the url of the SaaS instance that
    corresponds to the account_id field of a given payment and send the payment
    data there. DoesNotExist errors will be returned to the caller.
    '''
    def route(self, data):
        try:
            self.dest = models.SaasInstance.objects.get(id=data['account_id'])
        except (models.SaasInstance.DoesNotExist) as does_not_exist:
            return does_not_exist
        return super().route(data)


class ReferenceIdRouter(Router):
    '''
    The ReferenceIdRouter has to retrieve customer identifiers from the known
    SaaS instances since this information will likely be located in their
    domain. As soon as an instance sends a confirmation, it will dispatch the
    payment data to that instance.

    NOTE: It is assumed that instances provide some kind of API to retrieve the
    required information. As there is no information about formats and calls,
    the router will focus on status codes exclusively.
    '''
    class ReferenceIdError(Exception):
        '''
        Custom error in case of unsuccessful localisation attempt.
        '''
        def __init__(self, reference_id):
            super().__init__()

    def route(self, data):
        # ReferenceIdError is returned to views if it occurs.
        try:
            self.dest = self.locate_reference_id(data['reference_id'])
        except self.ReferenceIdError as reference_id_error:
            return reference_id_error
        return super().route(data)

    def locate_reference_id(self, reference_id):
        # Retrieve all SaaS instances from model
        saas_instances = models.SaasInstance.objects.all()
        # Try to determine which instance holds a customer with the respective
        # reference_id.
        for instance in saas_instances:
            try:
                # This call depends on the instance API.
                response = requests.get(instance.url)
            except ConnectionError:
                continue
            # Some way of verifying confirmation, depends on API as well.
            if response.status_code == 200:
                return instance
        # reference_id could not be located. Raise custom error.
        raise self.ReferenceIdError(reference_id)
