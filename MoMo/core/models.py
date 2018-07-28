'''  Create models '''

from django.db import models
from datetime import datetime

# PaymentServiceProvider currently contains only the id and fullname of the PSP
class PaymentServiceProvider(models.Model):
    fullname = models.CharField(max_length=100)

# PspAdapter contains the id, the PSP it is used for and the port on
# which it is currently listening for incoming payment data. Note that this
# model refers to active adapters (not all adapters known). This structure may
# change in order to provide more transparency as well as consistent port 
# numbers for the adapters
class PspAdapter(models.Model):
    psp = models.ForeignKey(PaymentServiceProvider, on_delete=models.PROTECT)
    port = models.IntegerField(null=True)
    activated = models.BooleanField(default=False)

# SaasInstance contains id (account_id), fullname and the url used to send 
# payment data or retrieve information (e.g. for routing purposes) 
class SaasInstance(models.Model):
    fullname = models.CharField(max_length=100)
    url = models.URLField(default='')

# Payment contains id, reference_id (identifying individual customer, currently
# arbitrary), the time the data was received (by this core API), a reference to
# a SaasInstance and a reference to a PaymentServiceProvider
class Payment(models.Model):
    reference_id = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    date_received = models.DateTimeField(default=datetime.now)
    account_id = models.ForeignKey(SaasInstance, on_delete=models.PROTECT)
    psp = models.ForeignKey(PaymentServiceProvider, on_delete=models.PROTECT)
