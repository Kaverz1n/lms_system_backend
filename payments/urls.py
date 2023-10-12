from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import PaymentListAPIView, PaymentCreateAPIView, PaymentIntentCreateAPIView

app_name = PaymentsConfig.name

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payments_list'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('<str:subject_type>/<int:subject_pk>/pay/', PaymentIntentCreateAPIView.as_view(), name='payment_intent_create')
]
