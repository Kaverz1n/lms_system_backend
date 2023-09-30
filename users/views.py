from rest_framework import generics

from users.models import User
from users.serializers import UpdateUserSerializer, UserPaymentSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    '''
    Generic-класс для обновления пользователя
    '''
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()


class UserPaymentListAPIView(generics.ListAPIView):
    '''
    Generic-класс для обновления пользователя
    '''
    serializer_class = UserPaymentSerializer
    queryset = User.objects.all()
