from django.shortcuts import redirect

from django_filters.rest_framework import DjangoFilterBackend

from payments.models import Payment
from payments.serializers import PaymentHistorySerializer, PaymentSerializer
from payments.services import create_payment_session

from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from school.models import Course, Lesson

from users.models import User


class PaymentListAPIView(generics.ListAPIView):
    '''
    Просмотр всех объектов Payment
    '''
    serializer_class = PaymentHistorySerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method',)
    ordering_fields = ('date',)


class PaymentCreateAPIView(generics.CreateAPIView):
    '''
    Создание информации о платеже
    '''
    serializer_class = PaymentHistorySerializer

    def get(self, request, *args, **kwargs) -> None:
        user = User.objects.get(pk=request.query_params.get('user'))
        title = request.query_params.get('title')
        amount = request.query_params.get('amount')
        subject_type = request.query_params.get('subject_type')
        subject = Course if subject_type == 'course' else Lesson
        subject_obj = subject.objects.get(title=title)

        data = {
            'user': user,
            'amount': amount,
            subject_type: subject_obj,
        }

        Payment.objects.create(**data)

        return redirect('payments:payments_list')


class PaymentIntentCreateAPIView(generics.CreateAPIView):
    '''
    Создание платежа для покупки курса/урока
    '''

    def post(self, request, *args, **kwargs) -> Response:
        serializer = PaymentSerializer(data=request.data, context={'view': self})

        if serializer.is_valid():
            title = serializer.data['item_inf'][0]
            description = serializer.data['item_inf'][1]
            amount = serializer.data['item_inf'][2]

            return create_payment_session(title, description, amount, request, kwargs)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
