'''
Create class-based API views. Generic views contained from rest_framework make
our life much easier (extended request-object, flexible formats, less code
duplication, verbose status codes, etc.).
Wired views up by connecting path to function APIView.as_view() in urls.py
'''
from rest_framework import generics

from core.models import (
    Payment,
    PspAdapter,
    PaymentServiceProvider,
    SaasInstance
)
from core.serializers import (
    PaymentSerializer,
    PspAdapterSerializer,
    PspSerializer,
    SaasInstanceSerializer
)
#import core.hooks

class PaymentList(generics.ListCreateAPIView):
    '''
    Payment provides methods GET (list) and POST.
    PUT and DELETE are not implemented seeing that this data is stored for
    compliance reasons and should not be tampered with.
    '''
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # Perform_create() functions provide a hook for custom behaviour (e.g.
    # routing the received payment data to the respective SaasInstance)
    def perform_create(self, serializer):
        # TODO: Route to SaasInstance
        serializer.save()

class PspAdapterList(generics.ListCreateAPIView):
    '''
    Methods GET (list) and POST for model PspAdapter
    '''
    queryset = PspAdapter.objects.all()
    serializer_class = PspAdapterSerializer

class PspAdapterAtomic(generics.RetrieveUpdateDestroyAPIView):
    '''
    Methods GET (byId), PUT and DELETE for model PspAdapter
    '''
    queryset = PspAdapter.objects.all()
    serializer_class = PspAdapterSerializer

class PspList(generics.ListCreateAPIView):
    '''
    Methods GET (list) and POST for model PaymentServiceProvider.
    '''
    queryset = PaymentServiceProvider.objects.all()
    serializer_class = PspSerializer

class PspAtomic(generics.RetrieveDestroyAPIView):
    '''
    Methods GET (byId) and DELETE for model PaymentServiceProvider
    '''
    queryset = PaymentServiceProvider.objects.all()
    serializer_class = PspSerializer

class SaasInstanceList(generics.ListCreateAPIView):
    '''
    Methods GET (list) and POST for model SaasInstance.
    '''
    queryset = SaasInstance.objects.all()
    serializer_class = SaasInstanceSerializer

class SaasInstanceAtomic(generics.RetrieveDestroyAPIView):
    '''
    Methods GET (byId) and DELETE for model SaasInstance
    '''
    queryset = SaasInstance.objects.all()
    serializer_class = SaasInstanceSerializer
