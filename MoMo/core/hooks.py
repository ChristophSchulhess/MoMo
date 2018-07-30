'''
Define hooks called in APIView methods such as perform_create()
'''
from core import routers

def route_by_account(data):
    '''
    Route payment data by account_id.
    '''
    return routers.AccountIdRouter().route(data)

def route_by_reference(data):
    '''
    Route payment data by reference_id.
    '''
    return routers.ReferenceIdRouter().route(data)
