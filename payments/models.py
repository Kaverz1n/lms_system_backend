from django.db import models

from school.models import Course, Lesson, NULLABLE
from users.models import User


class Payment(models.Model):
    '''
    Модель истории платежей пользователей
    '''
    PAYMENT_CHOICE = (
        ('Cash', 'Наличные'),
        ('Card', 'Перевод'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='payment_user')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс', related_name='payment_course',
                               **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Урок', related_name='payment_lesson',
                               **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    method = models.CharField(max_length=4, choices=PAYMENT_CHOICE, verbose_name='Метод')

    def __str__(self) -> str:
        return f'{self.user.email}'

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
