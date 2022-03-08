import logging
import os
from logging.handlers import RotatingFileHandler

import requests
from django.utils import timezone

from .models import Message

logging.basicConfig(
    level=logging.DEBUG,
    filename=__file__ + '.log',
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s',
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('my_logger.log', maxBytes=50000000,
                              backupCount=5)
logger.addHandler(handler)

URL = 'https://probe.fbrq.cloud/v1/send/'
TOKEN = os.environ.get('API_TOKEN')
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def send_msg(msgld, phone, text, ):
    massage = save_results(mailing=msgld)
    data = {
        'id': massage.id,
        'phone': phone,
        'text': text
    }
    try:
        response = requests.post(
            url=URL,
            headers=HEADERS,
            json=data
        )
        if msgld.start_datetime > msgld.finish_datetime:
            logger.debug(f'Отправка рассылки {msgld.id}')
            send_msg(data)
            logger.debug(f'Отправка рассылки {msgld.id} завершена')
        massage.sending_status = response.status
    except requests.exceptions.ConnectionError as e:
        massage.sending_status = 'Ошибка подключения'
        logger.exception(f'Ошибка {e}')
    massage.save()


def save_results(mailing, status=None):
    return Message.objects.create(
        date_time=timezone.now(),
        status=status,
        mailing=mailing
    )
