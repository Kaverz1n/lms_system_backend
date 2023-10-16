from payments.models import Payment

from rest_framework import serializers

from school.models import Course, Lesson

from typing import Any


class PaymentSerializer(serializers.Serializer):
    '''
    Сериализатор для обработки платежа
    '''
    item_inf = serializers.SerializerMethodField()

    def get_item_inf(self, instance) -> [Any]:
        information = []
        subject_type = self.context['view'].kwargs.get('subject_type')
        subject_pk = self.context['view'].kwargs.get('subject_pk')

        if subject_type == 'course':
            subject = Course
        elif subject_type == 'lesson':
            subject = Lesson
        else:
            raise serializers.ValidationError('Ошибка оплаты!')

        subject_obj = subject.objects.get(pk=subject_pk)

        information.append(subject_obj.title)
        information.append(subject_obj.description)
        information.append(subject_obj.price)

        return information


class PaymentHistorySerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели проведенного платежа
    '''

    class Meta:
        model = Payment
        fields = (
            'user',
            'date',
            'course',
            'lesson',
            'amount',
            'method',
        )
