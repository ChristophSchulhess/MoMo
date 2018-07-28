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

# Create your views here.

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def perform_create(self, serializer):
        # TODO: Route to SaasInstance
        serializer.save()

class PspAdapterList(generics.ListCreateAPIView):
    queryset = PspAdapter.objects.all()
    serializer_class = PspAdapterSerializer

    def perform_create(self, serializer):
        serializer.validated_data = hooks.port_select(serializer.validated_data)
        serializer.save()

class PspAdapterAtomic(generics.RetrieveDestroyAPIView):
    queryset = PspAdapter.objects.all()
    serializer_class = PspAdapterSerializer

class PspList(generics.ListCreateAPIView):
    queryset = PaymentServiceProvider.objects.all()
    serializer_class = PspSerializer

class PspAtomic(generics.RetrieveDestroyAPIView):
    queryset = PaymentServiceProvider.objects.all()
    serializer_class = PspSerializer

class SaasInstanceList(generics.ListCreateAPIView):
    queryset = SaasInstance.objects.all()
    serializer_class = SaasInstanceSerializer

class SaasInstanceAtomic(generics.RetrieveDestroyAPIView):
    queryset = SaasInstance.objects.all()
    serializer_class = SaasInstanceSerializer