'''  Wire up paths with (API)views '''

from django.urls import path
from core import views

PAYMENT_PATH = 'payment/'
PSP_PATH = 'payment_service_provider/'
PSP_ADAPTER_PATH = 'psp_adapter/'
SAAS_INSTANCE_PATH = 'saas_instance/'

urlpatterns = [
    # Methods GET (list) and POST
    path(PAYMENT_PATH, views.PaymentList.as_view()),
    path(PSP_ADAPTER_PATH, views.PspAdapterList.as_view()),
    path(PSP_PATH, views.PspList.as_view()),
    path(SAAS_INSTANCE_PATH, views.SaasInstanceList.as_view()),

    # Atomic methods
    path('{}<int:id>'.format(PSP_ADAPTER_PATH),
        views.PspAdapterAtomic.as_view()),
    path('{}<int:id>'.format(PSP_PATH), views.PspAtomic.as_view()),
    path('{}<int:id>'.format(SAAS_INSTANCE_PATH),
        views.SaasInstanceAtomic.as_view())
]