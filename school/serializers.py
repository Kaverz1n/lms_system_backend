from rest_framework import serializers

from school.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели обучающего курса
    '''

    class Meta:
        model = Lesson
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        lesson = Lesson.objects.create(**validated_data, user=user)

        return lesson


class CourseSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели обучающего курса
    '''
    lessons_quantity = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            'pk',
            'title',
            'description',
            'image',
            'lessons_quantity',
            'lessons',
            'user',
        )

    def get_lessons_quantity(self, instance):
        return Lesson.objects.filter(course=instance).count()

    def create(self, validated_data):
        lessons = validated_data.pop('lessons')
        user = self.context['request'].user
        course = Course.objects.create(**validated_data, user=user)

        for lesson in lessons:
            Lesson.objects.create(**lesson, course=course, user=user)

        return course

    def update(self, instance, validated_data):
        lessons = validated_data.pop('lessons')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        Lesson.objects.filter(course=instance).delete()

        for lessons in lessons:
            Lesson.objects.create(**lessons, course=instance, user=instance.user)

        return instance
