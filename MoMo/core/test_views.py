'''
Create view tests here.
'''
from django.db.models.deletion import ProtectedError
from rest_framework import status
from rest_framework.test import APITestCase
from core import models

class PaymentTest(APITestCase):
    '''
    Test case for Payment API POST and GET call.
    '''
    fixtures = ['core']

    def test_payment_is_created(self):
        '''
        Test whether a simple POST call with suitable data creates a new entry
        in the respective model. Similar for all models.
        '''
        data = {
            'reference_id': 'mister_blue',
            'amount': 42.0,
            'account_id': 1,
            'psp': 2
        }
        response = self.client.post('/payment/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Fixture contains two payment entries, thus count should be 3
        self.assertEqual(models.Payment.objects.count(), 3)

    def test_payment_list_is_retrieved(self):
        '''
        Test whether a GET call (non-atomic) retrieves the expected set of
        entries. Similar for all models.
        '''
        fixtures_payment_count = 4
        response = self.client.get('/payment/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), fixtures_payment_count)

class PaymentServiceProviderTest(APITestCase):
    '''
    Test case for PaymentServiceProvider API POST, GET, DELETE, PUT calls
    '''
    fixtures = ['core']

    def test_psp_is_created(self):
        '''
        See PaymentTest
        '''
        data = {'fullname': 'Zeitsparkasse'}
        response = self.client.post('/payment_service_provider/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Fixture contains two payment service providers => count should be 3
        self.assertEqual(models.PaymentServiceProvider.objects.count(), 3)

    def test_no_duplicate_fullname(self):
        '''
        Test unique constraints of model. Similar for SaasInstance (url)
        '''
        data = {'fullname': 'Zeitsparkasse'}
        models.PaymentServiceProvider.objects.create(fullname='Zeitsparkasse')
        response = self.client.post('/payment_service_provider/', data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['fullname'][0],
            'payment service provider with this fullname already exists.')

    def test_psp_list_is_retrieved(self):
        '''
        See PaymentTest
        '''
        response = self.client.get('/payment_service_provider/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_psp_is_retrieved(self):
        '''
        Test whether a GET call (atomic) retrieves the expected entry. Similar
        for SaasInstance and PspAdapter
        '''
        psp_id = 1
        response = self.client.get('/payment_service_provider/{}/'.format(
            psp_id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], psp_id)

    def test_psp_is_protected(self):
        '''
        Test whether deleting an entry that is references with
        on_delete=models.PROTECT raises a ProtectedError. Similar for
        SaasInstance
        '''
        psp_id = 1
        with self.assertRaises(ProtectedError):
            self.client.delete('/payment_service_provider/{}/'.format(psp_id))

    def test_psp_is_deleted(self):
        '''
        Test whether an entry is deleted when no foreign keys depend on it.
        Similar for SaasInstance.
        '''
        psp_id = 1
        # Delete refering entries in other models first
        models.Payment.objects.filter(psp=psp_id).delete()
        models.PspAdapter.objects.filter(psp=psp_id).delete()

        response = self.client.delete(
            '/payment_service_provider/{}/'.format(psp_id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# TODO: Complete test suite for all models similar to the above cases.
