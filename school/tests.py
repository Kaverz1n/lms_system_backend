from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from school.models import Course, Lesson, Subscription
from users.models import User


class CourseTestCase(APITestCase):
    '''
    Тестирования CRUD модели Course
    '''

    def setUp(self) -> None:
        call_command('flush', interactive=False)
        self.user = User.objects.create(email='admin', password='admin', is_superuser=True)
        self.token = f'Bearer {AccessToken.for_user(self.user)}'
        self.course = Course.objects.create(title="TEST", description="TEST", user=self.user)

    def test_create(self) -> None:
        '''
        Тестирование создания курса
        '''
        data = {
            "title": "TEST1",
            "description": "TEST1",
        }
        response = self.client.post(
            '/api/courses/',
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 2, 'title': 'TEST1', 'description': 'TEST1',
                'image': 'http://testserver/media/courses/default.jpg',
                'lessons_quantity': 0, 'lessons': [], 'user': 1
            }
        )

    def test_list(self) -> None:
        '''
        Тестирование вывода списка всех курсов
        '''
        Course.objects.create(title='TEST1', description='TEST1', user=self.user)

        response = self.client.get(
            '/api/courses/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 2, 'next': None, 'previous': None, 'results':
                [
                    {
                        'pk': 1, 'title': 'TEST', 'description': 'TEST',
                        'image': 'http://testserver/media/courses/default.jpg',
                        'lessons_quantity': 0, 'lessons': [], 'user': 1
                    },
                    {
                        'pk': 2, 'title': 'TEST1', 'description': 'TEST1',
                        'image': 'http://testserver/media/courses/default.jpg',
                        'lessons_quantity': 0, 'lessons': [], 'user': 1
                    }
                ]
            }
        )

    def test_retrieve(self) -> None:
        '''
        Тестирование вывода одного курса
        '''
        response = self.client.get(
            '/api/courses/1/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1, 'title': 'TEST', 'description': 'TEST',
                'image': 'http://testserver/media/courses/default.jpg',
                'lessons_quantity': 0, 'lessons': [], 'user': 1,
                'current_user': 1, 'is_subscribed': False
            }
        )

    def test_update(self) -> None:
        '''
        Тестирование обновления курса
        '''
        data = {
            "title": "TEST2"
        }
        response = self.client.patch(
            '/api/courses/1/',
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1, 'title': 'TEST2', 'description': 'TEST',
                'image': 'http://testserver/media/courses/default.jpg',
                'lessons_quantity': 0, 'lessons': [], 'user': 1
            }
        )

        data = {
            "title": "TEST2",
            "description": "TEST2"
        }

        response = self.client.put(
            '/api/courses/1/',
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1, 'title': 'TEST2', 'description': 'TEST2',
                'image': 'http://testserver/media/courses/default.jpg',
                'lessons_quantity': 0, 'lessons': [], 'user': 1
            }
        )

    def test_destroy(self) -> None:
        '''
        Тестирование удаления курса
        '''
        response = self.client.delete(
            '/api/courses/1/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            list(Course.objects.all()),
            []
        )

    def tearDown(self):
        pass


class LessonTestCase(APITestCase):
    '''
    Тестирования CRUD модели Lesson
    '''

    def setUp(self) -> None:
        call_command('flush', interactive=False)
        self.user = User.objects.create(email='admin', password='admin', is_superuser=True)
        self.token = f'Bearer {AccessToken.for_user(self.user)}'
        self.lesson = Lesson.objects.create(title="TEST", description="TEST", video_url='TEST', user=self.user)

    def test_create(self) -> None:
        '''
        Тестирование создания урока
        '''
        data = {
            "title": "TEST1",
            "description": "TEST1",
            "video_url": "https://www.youtube.com/watch?TEST"
        }
        response = self.client.post(
            '/api/lessons/create/',
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                "pk": 2, "title": "TEST1", "description": "TEST1",
                "image": "http://testserver/media/lessons/default.jpg",
                "video_url": "https://www.youtube.com/watch?TEST", "course": None,
                "user": 1
            }
        )

    def test_list(self) -> None:
        '''
        Тестирование вывода списка всех урооков
        '''
        Lesson.objects.create(title='TEST', description='TEST', video_url='TEST', user=self.user)

        response = self.client.get(
            '/api/lessons/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 2, 'next': None, 'previous': None, 'results':
                [
                    {
                        "pk": 1, "title": "TEST", "description": "TEST",
                        "image": "http://testserver/media/lessons/default.jpg",
                        "video_url": "TEST", "course": None,
                        "user": 1
                    },
                    {
                        "pk": 2, "title": "TEST", "description": "TEST",
                        "image": "http://testserver/media/lessons/default.jpg",
                        "video_url": "TEST", "course": None,
                        "user": 1
                    }
                ]
            }
        )

    def test_retrieve(self) -> None:
        '''
        Тестирование вывода одного урока
        '''
        response = self.client.get(
            '/api/lessons/1/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "pk": 1, "title": "TEST", "description": "TEST",
                "image": "http://testserver/media/lessons/default.jpg",
                "video_url": "TEST", "course": None,
                "user": 1
            }
        )

    def test_update(self) -> None:
        '''
        Тестирование обновления урока
        '''
        data = {
            "title": "TEST2",
            "video_url": "https://www.youtube.com/watch?TEST"
        }
        response = self.client.patch(
            '/api/lessons/update/1/',
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "pk": 1, "title": "TEST2", "description": "TEST",
                "image": "http://testserver/media/lessons/default.jpg",
                "video_url": "https://www.youtube.com/watch?TEST", "course": None,
                "user": 1
            }
        )

        data = {
            "title": "TEST2",
            "description": "TEST2",
            "video_url": "https://www.youtube.com/watch?TEST",
        }

        response = self.client.put(
            '/api/lessons/update/1/',
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.json(),
            {
                "pk": 1, "title": "TEST2", "description": "TEST2",
                "image": "http://testserver/media/lessons/default.jpg",
                "video_url": "https://www.youtube.com/watch?TEST", "course": None,
                "user": 1
            }
        )

    def test_destroy(self) -> None:
        '''
        Тестирование удаления урока
        '''
        response = self.client.delete(
            '/api/lessons/destroy/1/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            list(Lesson.objects.all()),
            []
        )

    def tearDown(self):
        pass


class SubscriptionTestCase(APITestCase):
    '''
    Тестирование подписки на курс
    '''

    def setUp(self) -> None:
        call_command('flush', interactive=False)
        self.user = User.objects.create(email='admin', password='admin', is_superuser=True)
        self.token = f'Bearer {AccessToken.for_user(self.user)}'
        self.course = Course.objects.create(title="TEST", description="TEST", user=self.user)

    def test_subscribe(self):
        '''
        Тестирование подписки на курс
        '''
        response = self.client.get(
            '/api/courses/1/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1, 'title': 'TEST', 'description': 'TEST',
                'image': 'http://testserver/media/courses/default.jpg',
                'lessons_quantity': 0, 'lessons': [], 'user': 1,
                'current_user': 1, 'is_subscribed': False
            }
        )

        self.client.post(
            '/api/courses/1/subscribe/',
            HTTP_AUTHORIZATION=self.token
        )

        response = self.client.get(
            '/api/courses/1/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1, 'title': 'TEST', 'description': 'TEST',
                'image': 'http://testserver/media/courses/default.jpg',
                'lessons_quantity': 0, 'lessons': [], 'user': 1,
                'current_user': 1, 'is_subscribed': True
            }
        )

    def test_unsubscribe(self):
        '''
        Тестирование отписки от курса
        '''
        Subscription.objects.create(user=self.user, course=self.course)

        response = self.client.get(
            '/api/courses/1/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1, 'title': 'TEST', 'description': 'TEST',
                'image': 'http://testserver/media/courses/default.jpg',
                'lessons_quantity': 0, 'lessons': [], 'user': 1,
                'current_user': 1, 'is_subscribed': True
            }
        )

        self.client.delete(
            '/api/courses/1/unsubscribe/',
            HTTP_AUTHORIZATION=self.token
        )

        response = self.client.get(
            '/api/courses/1/',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1, 'title': 'TEST', 'description': 'TEST',
                'image': 'http://testserver/media/courses/default.jpg',
                'lessons_quantity': 0, 'lessons': [], 'user': 1,
                'current_user': 1, 'is_subscribed': False
            }
        )

    def tearDown(self) -> None:
        pass
