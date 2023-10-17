import datetime

from celery import shared_task

from django.core.mail import send_mail

from lms_system import settings

from school.models import Subscription, Course

from users.models import User


@shared_task
def update_course_send_mail(course_pk: int) -> None:
    '''
    Отправляет e-mail об обновлении курса всем
    подписчикам данного курса
    '''
    course = Course.objects.get(pk=course_pk)
    subscriptions = Subscription.objects.filter(course=course)
    subscribers_emails = [subscriber.user.email for subscriber in subscriptions]

    send_mail(
        subject=f'Курс {course.title} обновлён!',
        message=f'Вы ранее оформляли подписку на курс {course.title}! В некоторые материалы были '
                f'внесены поправки! Вы можете ознакомиться с ними в личном кабинете!',
        from_email=settings.EMAIL_ADMIN,
        recipient_list=subscribers_emails
    )


@shared_task
def block_users() -> None:
    '''
    Блокирует пользователей, если пользователь
    не заходил более месяца
    '''
    month = 30
    now = datetime.datetime.now()
    users = User.objects.all()

    for user in users:
        if user.last_login:
            days_logout = int((now.timestamp() - user.last_login.timestamp()) // 86400)
            if days_logout > month:
                user.is_active = False
                user.save()
