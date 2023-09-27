from PIL import Image
from django.db import models

from school.services import resize_image

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    '''
    Модель обучающего курса сервиса
    '''
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='cources/', default='courses/default.jpg', verbose_name='Превью', **NULLABLE)

    def __str__(self) -> str:
        return f'{self.title}'

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        resized_image = resize_image(img, (1200, 800))
        resized_image.save(self.image.path)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    '''
    Модель обучаюещего урока сервиса
    '''
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='lessons/', default='lessons/default.jpg', verbose_name='Превью', **NULLABLE)
    video_url = models.TextField(verbose_name='Видео-url')

    def __str__(self) -> str:
        return f'{self.title}'

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        resized_image = resize_image(img, (1200, 800))
        resized_image.save(self.image.path)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
