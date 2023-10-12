from rest_framework import generics

from users.models import User
from users.serializers import (
    UpdateUserSerializer,
    UserProfileSerializer,
    UserProfileNoDataSerializer
)


class UserUpdateAPIView(generics.UpdateAPIView):
    '''
    Обновление пользователя
    '''
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()


class UserProfileRetrieveAPIView(generics.RetrieveAPIView):
    '''
    Просмотр профиля пользователя
    '''
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user.pk == self.get_object().pk:
            return UserProfileSerializer
        return UserProfileNoDataSerializer
