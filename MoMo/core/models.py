from django.db import models
from datetime import datetime

class PaymentServiceProvider(models.Model):
    fullname = models.CharField(max_length=100)

class SaasInstance(models.Model):
    fullname = models.CharField(max_length=100)
    hostname = models.CharField(max_length=50, default='')
    address = models.GenericIPAddressField(protocol='both', null=True)

class Payment(models.Model):
    reference_id = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    date_received = models.DateTimeField(default=datetime.now)
    account_id = models.ForeignKey(SaasInstance, on_delete=models.PROTECT)
    psp = models.ForeignKey(PaymentServiceProvider, on_delete=models.PROTECT)
