import json

from django_celery_beat.models import PeriodicTask, IntervalSchedule

from PIL import Image


def resize_image(img: Image, size: tuple) -> Image:
    '''
    Фунция изменяет размер на переданный, если размер
    переданого изображения не соответствует ему.
    :param img: объект класса Image
    :param size: кортеж состоящий из желаемой высоты и ширины
    картинки
    :return: объект класса Image
    '''
    try:
        if img.width != size[0] or img.height != size[1]:
            resized_image = img.resize(size)

            return resized_image

        return img
    except IndexError:
        print('Неверное указание размера изображения')
    except TypeError:
        print('Ошибка изменения размера изображения')


def add_schedule(course_pk: int) -> None:
    '''
    Добавляет переодичную одноразовую задачу на оповещение
    об обновлении курса
    :param course_pk: Course.pk
    '''
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=4,
        period=IntervalSchedule.HOURS,
    )

    task, created = PeriodicTask.objects.get_or_create(
        interval=schedule,
        name=f'Sending E-mail of updating course {course_pk}',
        task='school.tasks.update_course_send_mail',
        args=json.dumps([course_pk]),
        kwargs=json.dumps({}),
        expires=None,
        one_off=True
    )

    if not created:
        task.enabled = True
        task.save()
