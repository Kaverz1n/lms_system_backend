from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    '''
    Команда для создания суперпользователя
    '''

    def handle(self, *args, **options) -> None:
        try:
            user = User.objects.create(
                email='admin@yandex.ru',
                phone='8 999 999 99-99',
                city='Moscow',
                is_staff=True,
                is_superuser=True,
            )
            user.set_password('admin')
            user.save()
            self.stdout.write('Администратор успешно создан!')
        except Exception as e:
            self.stderr.write(f'Ошибка создания администратора!\nОшибка: {e}')
