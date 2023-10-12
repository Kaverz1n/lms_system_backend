from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from school.models import Course, Lesson, Subscription
from school.paginators import CoursePaginator, LessonPaginator
from school.permissions import IsModeratorOrOwner
from school.serializers import (
    CourseSerializer, LessonSerializer, SubscriptionSerializer, UserCourseSerializer
)


class CourseViewSet(viewsets.ModelViewSet):
    '''
    ViewSet для модели обучающего курса
    '''
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]
    pagination_class = CoursePaginator

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserCourseSerializer
        return CourseSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    '''
    Cоздание объекта Lesson
    '''
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    '''
    Обновление объекта Lesson
    '''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]


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

    def get_object(self):
        course_pk = self.kwargs.get('course_pk')
        course = Course.objects.get(pk=course_pk)
        object_ = Subscription.objects.get(course=course)

        return object_
