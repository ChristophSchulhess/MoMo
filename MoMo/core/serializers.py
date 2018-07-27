from rest_framework import serializers
from core.models import Payment, PaymentServiceProvider, SaasInstance

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