'''
Create models
'''
from datetime import datetime
from django.db import models

class PaymentServiceProvider(models.Model):
    '''
    PaymentServiceProvider currently contains only the id and fullname of the
    PSP
    '''
    fullname = models.CharField(max_length=100, unique=True)

class PspAdapter(models.Model):
    '''
    PspAdapter contains the id, the PSP it is used for, the port on which it
    is currently listening for incoming payment data and an activated flag.
    '''
    psp = models.ForeignKey(PaymentServiceProvider, on_delete=models.PROTECT)
    port = models.IntegerField(null=True)
    activated = models.BooleanField(default=False)

    class Meta:
        unique_together = ('psp', 'port')

class SaasInstance(models.Model):
    '''
    SaasInstance contains id (account_id), fullname and the url used to send
    payment data or retrieve information (e.g. for routing purposes)
    '''
    fullname = models.CharField(max_length=100)
    url = models.URLField(default='')

    class Meta:
        unique_together = ('fullname', 'url')

class Payment(models.Model):
    '''
    Payment contains id, reference_id (identifying individual customer,
    currently arbitrary), the time the data was received (by this core API), a
    reference to a SaasInstance and a reference to a PaymentServiceProvider
    '''
    reference_id = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    date_received = models.DateTimeField(default=datetime.now)
    account_id = models.ForeignKey(SaasInstance, on_delete=models.PROTECT)
    psp = models.ForeignKey(PaymentServiceProvider, on_delete=models.PROTECT)
