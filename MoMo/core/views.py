'''
Create class-based API views. Generic views contained from rest_framework make
our life much easier (extended request-object, flexible formats, less code
duplication, verbose status codes, etc.).
Wired views up by connecting path to function APIView.as_view() in urls.py
'''

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

from rest_framework import generics
import core.hooks as hooks

# Payment provides methods GET (list) and POST.
# PUT and DELETE are not implemented seeing that this data is stored for
# compliance reasons and should not be tampered with
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # Perform_create() functions provide a hook for custom behaviour (e.g.
    # routing the received payment data to the respective SaasInstance)
    def perform_create(self, serializer):
        # TODO: Route to SaasInstance
        serializer.save()

# Methods GET (list) and POST for model PspAdapter
class PspAdapterList(generics.ListCreateAPIView):
    queryset = PspAdapter.objects.all()
    serializer_class = PspAdapterSerializer

    # Hook for selecting free port to host adapter service. This can be seen as
    # a PoC feature for create hooks and will probably change in the future
    def perform_create(self, serializer):
        serializer.validated_data = hooks.port_select(serializer.validated_data)
        serializer.save()

# Methods GET (byId) and DELETE for model PspAdapter
class PspAdapterAtomic(generics.RetrieveUpdateDestroyAPIView):
    queryset = PspAdapter.objects.all()
    serializer_class = PspAdapterSerializer

# Methods GET (list) and POST for model PaymentServiceProvider. Currently no
# hooks.
class PspList(generics.ListCreateAPIView):
    queryset = PaymentServiceProvider.objects.all()
    serializer_class = PspSerializer

# Methods GET (byId) and DELETE for model PaymentServiceProvider
class PspAtomic(generics.RetrieveDestroyAPIView):
    queryset = PaymentServiceProvider.objects.all()
    serializer_class = PspSerializer

# Methods GET (list) and POST for model SaasInstance. Currently no
# hooks.
class SaasInstanceList(generics.ListCreateAPIView):
    queryset = SaasInstance.objects.all()
    serializer_class = SaasInstanceSerializer

# Methods GET (byId) and DELETE for model SaasInstance
class SaasInstanceAtomic(generics.RetrieveDestroyAPIView):
    queryset = SaasInstance.objects.all()
    serializer_class = SaasInstanceSerializer