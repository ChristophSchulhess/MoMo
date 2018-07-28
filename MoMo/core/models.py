from django.db import models
from datetime import datetime

class PaymentServiceProvider(models.Model):
    fullname = models.CharField(max_length=100)

class PspAdapter(models.Model):
    psp = models.ForeignKey(PaymentServiceProvider, on_delete=models.PROTECT)
    port = models.IntegerField(null=True)

class SaasInstance(models.Model):
    fullname = models.CharField(max_length=100)
    url = models.URLField(default='')

class Payment(models.Model):
    reference_id = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    date_received = models.DateTimeField(default=datetime.now)
    account_id = models.ForeignKey(SaasInstance, on_delete=models.PROTECT)
    psp = models.ForeignKey(PaymentServiceProvider, on_delete=models.PROTECT)
