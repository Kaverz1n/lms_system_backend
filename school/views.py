from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from school.services import add_schedule
from school.models import Course, Lesson, Subscription
from school.paginators import CoursePaginator, LessonPaginator
from school.permissions import IsModeratorOrOwner
from school.serializers import (
    CourseSerializer, LessonSerializer, SubscriptionSerializer, UserCourseSerializer
)

from typing import Type


class CourseViewSet(viewsets.ModelViewSet):
    '''
    ViewSet для модели обучающего курса
    '''
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]
    pagination_class = CoursePaginator

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == 'retrieve':
            return UserCourseSerializer
        return CourseSerializer

    def update(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        add_schedule(course_pk=instance.pk)

        return Response(serializer.data)


class LessonCreateAPIView(generics.CreateAPIView):
    '''
    Cоздание объекта Lesson
    '''
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        try:
            course_pk = serializer.instance.course.pk
            add_schedule(course_pk=course_pk)
        except AttributeError:
            pass

        return Response(serializer.data)


class LessonUpdateAPIView(generics.UpdateAPIView):
    '''
    Обновление объекта Lesson
    '''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]

    def update(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        try:
            course_pk = instance.course.pk
            add_schedule(course_pk=course_pk)
        except AttributeError:
            pass

        return Response(serializer.data)


class LessonListAPIView(generics.ListAPIView):
    '''
    Просмотр всех объектов Lesson
    '''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    '''
    Просмотр одного объекта Lesson
    '''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    '''
    Удаление одного объекта Lesson
    '''
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]

    def destroy(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance)

        try:
            course_pk = instance.course.pk
            add_schedule(course_pk=course_pk)
        except AttributeError:
            pass

        return Response(serializer.data)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    '''
    Ссоздание подписки на курс
    '''
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    '''
    Удаление подписки на курс
    '''
    queryset = Subscription.objects.all()

    def get_object(self) -> Subscription:
        user = self.request.user
        course_pk = self.kwargs.get('course_pk')
        course = Course.objects.get(pk=course_pk)
        object_ = Subscription.objects.get(course=course, user=user)

        return object_
