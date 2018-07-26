from django.db import models

class PaymentServiceProvider(models.Model):
    fullname = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

class SaasInstance(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.GenericIpAddressField(protocol='both')

class Payment(models.Model):
    reference_id = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    date_received = models.DateTimeField()
    account_id = models.ForeignKey(SaasInstance)
    psp = models.ForeignKey(PaymentServiceProvider)
