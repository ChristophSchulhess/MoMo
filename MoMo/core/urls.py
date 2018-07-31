'''
Wire up paths with (API)views
'''

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    # Methods GET (list) and POST
    url(r'^payment/$', views.PaymentList.as_view()),
    url(r'^psp_adapter/$', views.PspAdapterList.as_view()),
    url(r'^payment_service_provider/$', views.PspList.as_view()),
    url(r'^saas_instance/$', views.SaasInstanceList.as_view()),

    # Atomic methods
    url(r'^psp_adapter/(?P<pk>[0-9]+)/$', views.PspAdapterAtomic.as_view()),
    url(r'^payment_service_provider/(?P<pk>[0-9]+)/$',
        views.PspAtomic.as_view()),
    url(r'^saas_instance/(?P<pk>[0-9]+)/$', views.SaasInstanceAtomic.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
