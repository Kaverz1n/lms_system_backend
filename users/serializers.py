from rest_framework import serializers

from payments.serializers import PaymentSerializer
from users.models import User


class UpdateUserSerializer(serializers.ModelSerializer):
    '''
    Сериализтор для обновления пользователя сервиса
    '''

    class Meta:
        model = User
        fields = (
            'email',
            'phone',
            'first_name',
            'last_name',
            'city',
            'image',
        )


class UserPaymentSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели пользователя сервиса с историей платежей
    '''
    payment_history = PaymentSerializer(many=True, source='payment_user')

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'phone',
            'first_name',
            'last_name',
            'city',
            'image',
            'payment_history'
        )
