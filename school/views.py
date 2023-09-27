from rest_framework import viewsets, generics
from school.models import Course, Lesson
from school.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    '''
    ViewSet для модели обучающего курса
    '''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    '''
    Generic-класс для создания объекта Lesson
    '''
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    '''
    Generic-класс для обновления объекта Lesson
    '''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    '''
    Generic-класс для просмотра всех объектов Lesson
    '''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    '''
    Generic-класс для просмотра одного объекта Lesson
    '''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    '''
    Generic-класс для удаления одного объекта Lesson
    '''
    queryset = Lesson.objects.all()
