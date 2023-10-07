from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserProfileRetrieveAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

app_name = UsersConfig.name

urlpatterns = [
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('profile/<int:pk>/', UserProfileRetrieveAPIView.as_view(), name='user_payments_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
