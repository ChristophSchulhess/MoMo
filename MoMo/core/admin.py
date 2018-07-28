from django.contrib import admin

from .models import Payment, SaasInstance, PaymentServiceProvider, PspAdapter

# The models are registered for the admin app only for testing purposes.
# Productive environments are expect to interact via (then authenticated and
# authorized) API calls for monitoring and maintenance.
admin.site.register(Payment)
admin.site.register(SaasInstance)
admin.site.register(PaymentServiceProvider)
admin.site.register(PspAdapter)