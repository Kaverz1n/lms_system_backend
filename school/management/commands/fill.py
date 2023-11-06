from django.core.management import BaseCommand, call_command
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    '''
    Комманда для заполнения данными базу данных
    '''

    def handle(self, *args, **options) -> None:
        try:
            ContentType.objects.all().delete()
            call_command('loaddata', 'database_data.json')
        except Exception as e:
            self.stderr.write(f'Ошибка загрузки данных!\n{e}')
