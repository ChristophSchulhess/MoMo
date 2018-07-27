from django.contrib import admin

from .models import Payment, SaasInstance, PaymentServiceProvider

# Register your models here.
admin.site.register(Payment)
admin.site.register(SaasInstance)
admin.site.register(PaymentServiceProvider)