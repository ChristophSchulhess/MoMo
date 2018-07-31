'''
Create router tests here.
'''
from unittest import mock
from requests.exceptions import ConnectionError
from django.test import TestCase
from core import routers, models

# Data to be used for basically all the tests (with the exception of
# 'test_invalid_account_id()')
PAYMENT_DATA = {
    'reference_id': 'mister_brown',
    'psp': 1,
    'account_id': 1,
    'amount': 42.0
}

def mock_response(
        status=201,
        content=None,
        json_data=None,
        raise_for_status=None):
    '''
    Mock response which is used in most of the router tests since we don't want
    them to fail depending on whether a SaaS instance is actually live (or does
    even exist for that matter)
    '''
    mock_resp = mock.Mock()

    # Mock the requests response objects 'raise_for_status()' method
    mock_resp.raise_for_status = mock.Mock(return_value=raise_for_status)
    # Assign mock attributes
    mock_resp.status_code = status
    mock_resp.content = content
    # Mock the requests response objects 'json()' method
    if json_data:
        mock_resp.json = mock.Mock(return_value=json_data)
    return mock_resp

class RouterTestCase(TestCase):
    '''
    Test case for basic routing functionality
    '''
    @mock.patch('requests.post')
    def test_saas_instance_is_up(self, mock_post):
        '''
        Test whether a live SaaS instance leads to a return value (error state)
        of None.
        '''
        mock_resp = mock_response()
        mock_post.return_value = mock_resp

        router = routers.Router()
        router.dest = mock.Mock()

        error_state = router.route(PAYMENT_DATA)
        self.assertEqual(error_state, None)

    @mock.patch('requests.post')
    def test_saas_instance_is_down(self, mock_post):
        '''
        Test whether ConnectionError is returned if instance is down.
        '''
        mock_resp = mock_response()
        mock_post.return_value = mock_resp

        mock_post.side_effect = ConnectionError()

        router = routers.Router()
        router.dest = mock.Mock()

        error_state = router.route(PAYMENT_DATA)
        self.assertIsInstance(error_state, ConnectionError)

class AccountIdRouterTestCase(TestCase):
    '''
    Test case for AccountIdRouter
    '''
    fixtures = ['core']

    def test_invalid_account_id(self):
        '''
        Test whether a DoesNotExist error is returned when method is passed an
        invalid id. We don't need mocks here, since the request method should
        never be executed with invalid data.
        '''
        payment_data = dict.copy(PAYMENT_DATA)
        payment_data['account_id'] = 5000

        router = routers.AccountIdRouter()

        error_state = router.route(payment_data)
        self.assertIsInstance(error_state, models.SaasInstance.DoesNotExist)

class ReferenceIdRouterTestCase(TestCase):
    '''
    Test case for ReferenceIdRouter
    '''
    fixtures = ['core']

    @mock.patch('requests.get')
    def test_reference_id_exists(self, mock_get):
        '''
        Test whether 'locate_reference_id()' returns a SaaS instance when
        inquiring for a valid reference_id (i.e. one that is actually present in
        one of the instances' databases).
        '''
        mock_resp = mock_response(status=200)
        mock_get.return_value = mock_resp

        router = routers.ReferenceIdRouter()

        dest = router.locate_reference_id(PAYMENT_DATA['reference_id'])
        self.assertIsInstance(dest, models.SaasInstance)

    @mock.patch('requests.get')
    def test_reference_id_does_not_exist(self, mock_get):
        '''
        Test whether a custom exception is raised when no instance confirms the
        reference_id.
        '''
        mock_resp = mock_response(status=404)
        mock_get.return_value = mock_resp

        router = routers.ReferenceIdRouter()

        with self.assertRaises(routers.ReferenceIdRouter.ReferenceIdError):
            router.locate_reference_id(PAYMENT_DATA['reference_id'])
