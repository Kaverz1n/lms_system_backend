import stripe

from django.http import HttpRequest

from lms_system import settings

from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response

from typing import Any

from urllib.parse import quote


def create_payment_session(
        title: str, description: str, amount: int,
        request: HttpRequest, kwargs: dict[str: Any]
) -> Response:
    '''
    Создание сессии оплаты с помощью сервиса Stripe
    :param title: наименование товара
    :param description: описание товара
    :param amount: цена товара
    :param request: объект запроса HTTP
    :param kwargs: доп. аргументы
    :return: Response с url сессии оплаты
    '''
    stripe.api_key = settings.STRIPE_SK

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'product_data': {
                            'name': title,
                            'description': description,
                        },
                        'unit_amount': int(amount * 100),
                    },
                    'quantity': 1,
                }],
            success_url='http://' + request.get_host() + reverse('payments:payment_create') +
                        f'?subject_type={quote(kwargs.get("subject_type"), safe="")}&title='
                        f'{quote(title, safe="")}&amount={amount}&user={request.user.pk}',
            cancel_url='http://' + request.get_host() + reverse('payments:payments_list')
        )
        return Response({'url': session.url}, status=status.HTTP_201_CREATED)
    except stripe.error.StripeError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
