from payments.serializers import PaymentHistorySerializer

from rest_framework import serializers

from users.models import User


class UpdateUserSerializer(serializers.ModelSerializer):
    '''
    Сериализтор для обновления пользователя сервиса
    '''

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'password',
            'phone',
            'first_name',
            'last_name',
            'city',
            'image',
        )


class UserProfileSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для профиля пользователя сервиса
    '''
    payment_history = PaymentHistorySerializer(many=True, source='payment_user')

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'phone',
            'first_name',
            'last_name',
            'password',
            'city',
            'image',
            'payment_history'
        )


class UserProfileNoDataSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели пользователя со скртыми данными
    '''

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'phone',
            'first_name',
            'city',
            'image',
        )
