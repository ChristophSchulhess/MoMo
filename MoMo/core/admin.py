from django.contrib import admin

from .models import Payment, SaasInstance, PaymentServiceProvider, PspAdapter

# Register your models here.
admin.site.register(Payment)
admin.site.register(SaasInstance)
admin.site.register(PaymentServiceProvider)
admin.site.register(PspAdapter)