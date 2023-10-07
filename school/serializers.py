from rest_framework import serializers

from school.models import Course, Lesson, Subscription
from school.validators import VideoUrlValidator


class LessonSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели обучающего курса
    '''

    class Meta:
        model = Lesson
        fields = (
            'pk',
            'title',
            'description',
            'image',
            'video_url',
            'course',
            'user',
        )
        validators = [
            VideoUrlValidator(field='video_url')
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        lesson = Lesson.objects.create(**validated_data, user=user)

        return lesson


class CourseSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели обучающего курса
    '''
    lessons_quantity = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, required=False)

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
        lessons = validated_data.pop('lessons', [])
        user = self.context['request'].user
        course = Course.objects.create(**validated_data, user=user)

        for lesson in lessons:
            Lesson.objects.create(course=course, user=user, **lesson)

        return course

    def update(self, instance, validated_data):
        lessons = validated_data.pop('lessons', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        Lesson.objects.filter(course=instance).delete()

        for lesson in lessons:
            Lesson.objects.create(**lesson, course=instance, user=instance.user)

        return instance


class UserCourseSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели курса с информацией о подписке пользователя на курс
    '''
    lessons_quantity = serializers.SerializerMethodField()
    current_user = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_lessons_quantity(self, instance):
        return Lesson.objects.filter(course=instance).count()

    def get_current_user(self, obj):
        return self.context['request'].user.pk

    def get_is_subscribed(self, obj):
        current_user = self.get_current_user(obj)
        return Subscription.objects.filter(user=current_user, course=obj).exists()

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
            'current_user',
            'is_subscribed'
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели подписки на курс
    '''

    class Meta:
        model = Subscription
        fields = (
            'user',
            'course',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        course_pk = self.context['view'].kwargs.get('course_pk')
        course = Course.objects.get(pk=course_pk)

        subscription = Subscription.objects.get_or_create(user=user, course=course)

        return subscription
