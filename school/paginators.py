from rest_framework.pagination import PageNumberPagination


class CoursePaginator(PageNumberPagination):
    '''
    Пагинатор для модели курса
    '''
    page_size = 10
    page_size_query_param = 'per_page'
    max_page_size = 100


class LessonPaginator(PageNumberPagination):
    '''
    Пагинатор для модели урока
    '''
    page_size = 10
    page_size_query_param = 'per_page'
    max_page_size = 100
