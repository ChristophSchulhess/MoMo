from django.urls import path
from core import views

urlpatterns = [
    path('core/', views.payment_request),
]