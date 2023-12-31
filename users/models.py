from django.contrib.auth.models import AbstractUser
from django.db import models

from PIL import Image

from school.services import resize_image

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    '''
    Класс пользователей сервиса
    '''
    username = None
    email = models.EmailField(max_length=254, verbose_name='e-mail', unique=True)
    phone = models.CharField(max_length=25, verbose_name='телефон', unique=True)
    city = models.CharField(max_length=50, verbose_name='город')
    image = models.ImageField(upload_to='users/', default='users/default.jpg', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        resized_image = resize_image(img, (50, 50))
        resized_image.save(self.image.path)
