from rest_framework import serializers

from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели платежа
    '''

    class Meta:
        model = Payment
        fields = (
            'user',
            'date',
            'course',
            'lesson',
            'amount',
            'method',
        )
