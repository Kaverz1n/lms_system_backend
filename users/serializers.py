from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    '''
    Сериализтор для модели пользователя сервиса
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
