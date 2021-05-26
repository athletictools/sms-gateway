import logging
import aiohttp
from typing import List, Dict

from .base import BaseSmsBackend
from .models import Sms, SmsStatus
from .exceptions import SmsBackendError

logger = logging.getLogger(__name__)


class IqSmsBackend(BaseSmsBackend):
    __base_url = 'https://api.iqsms.ru/messages/v2/'
    timeout = 3

    def __init__(self, *, login: str, password: str, timeout=3):
        self.login = login
        self.password = password
        self.timeout = timeout

    async def __send_request(self, uri: str, params: Dict = None):
        params = params if params is None else {}
        params.update(login=self.login, password=self.password)
        url = f'{self.__base_url}{uri}.json'

        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            async with session.post(url, json=data) as resp:
                return await resp.json()

    async def validate_account(self):
        try:
            response = self.__send_request('balance')
            if response['status'] == 'ok':
                return True
        except KeyError:
            pass
        return False

    def make_iq_messages(self, messages: List[Sms]) -> List[Dict]:
        return [
            {
                'phone': message.phone_no,
                'clientId': '1',
                'text': message.text,
            } for msg in messages
        ]

    async def send(self, message: Sms) -> int:
        params = {
            'messages': self.make_iq_messages([message, ]),
        }
        result = self.__send_request('send', params)
        send_result = result['messages'][0]

        if send_result['status'] == 'accepted':
            return send_result['smscId']

        raise SmsBackendError(send_result['status'])

    async def mass_send(self, messages: List[Sms]) -> List[int]:
        params = {
            'messages': self.make_iq_messages(message),
        }
        result = self.__send_request('send', params)
        send_result = result['messages'][0]

        if send_result['status'] == 'accepted':
            return send_result['smscId']

        raise SmsBackendError(send_result['status'])

    async def get_status(self, sms_id: int) -> SmsStatus:
        params = {
            'messages': [
                {
                    'smscId': sms_id
                }
            ]
        }
        result = self.__send_request('status', params)
        status = result['messages'][0]['status']

        """
        Возможные статусы сообщения в IqSms
        queued 	        Сообщение находится в очереди
        delivered 	    Сообщение доставлено
        delivery error 	Ошибка доставки SMS
        smsc submit 	Сообщение доставлено в SMSC
        smsc reject 	Сообщение отвергнуто SMSC (номер заблокирован или не существует)
        incorrect id 	Неверный идентификатор сообщения
        """
        error_statuses = ['delivery error', 'smsc reject', 'incorrect id']

        if status == 'delivered':
            return SmsStatus.delivered

        if status in error_statuses:
            return SmsStatus.not_delivered

        return SmsStatus.sent
