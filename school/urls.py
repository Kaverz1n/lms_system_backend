from django.urls import path

from rest_framework import routers

from school.apps import SchoolConfig
from school.views import (
    CourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView, LessonUpdateAPIView,
    LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView
)

app_name = SchoolConfig.name

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
    path('courses/<int:course_pk>/subscribe/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('courses/<int:course_pk>/unsubscribe/', SubscriptionDestroyAPIView.as_view(), name='subscription_destroy'),
] + router.urls
