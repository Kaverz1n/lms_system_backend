from rest_framework import serializers

from school.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели обучающего курса
    '''

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели обучающего курса
    '''

    class Meta:
        model = Lesson
        fields = "__all__"
