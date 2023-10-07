from rest_framework.serializers import ValidationError


class VideoUrlValidator:
    '''
    Валидатор, отвечающий за проверку url: ссылка на видео
    должна вести только на видео с сайта youtube.com
    '''

    def __init__(self, field) -> None:
        self.field = field

    def __call__(self, value) -> None:
        video_url = dict(value).get(self.field)
        youtube_pattern = "https://www.youtube.com/"

        if youtube_pattern not in video_url:
            raise ValidationError('Недопустимая ссылка на сторонний ресурс')
