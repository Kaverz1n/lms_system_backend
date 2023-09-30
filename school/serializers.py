from rest_framework import serializers

from school.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели обучающего курса
    '''

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели обучающего курса
    '''
    lessons_quantity = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            'title',
            'description',
            'image',
            'lessons_quantity',
            'lessons',
        )

    def get_lessons_quantity(self, instance):
        return Lesson.objects.filter(course=instance).count()

    def create(self, validated_data):
        lessons = validated_data.pop('lessons')
        course = Course.objects.create(**validated_data)

        for lesson in lessons:
            Lesson.objects.create(**lesson, course=course)

        return course
