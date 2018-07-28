from rest_framework import serializers
from core.models import (
    Payment, 
    PspAdapter, 
    PaymentServiceProvider, 
    SaasInstance
)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id', 
            'reference_id', 
            'amount', 
            'date_received', 
            'account_id', 
            'psp'
        )

    def create(self, data):
        return Payment.objects.create(**data)

class PspAdapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PspAdapter
        fields = (
            'id',
            'psp',
            'port'
        )

    def create(self, data):
        return PspAdapter.objects.create(**data)

class PspSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentServiceProvider
        fields = (
            'id',
            'fullname'
        )

    def create(self, data):
        return PaymentServiceProvider.objects.create(**data)

class SaasInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaasInstance
        fields = (
            'id',
            'fullname',
            'url'
        )

    def create(self, data):
        return SaasInstance.objects.create(**data)