from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    '''
    Generic-класс для просмотра всех объектов Payment
    '''
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method',)
    ordering_fields = ('date',)
