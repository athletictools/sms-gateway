from typing import List


class BaseSmsBackend:
    def __init__(self):
        raise NotImplementedError

    async def send(self, message: Sms) -> int:
        """
        Sending single sms
        :param message: Sms
        :return: Internal id for checking status
        """
        raise NotImplementedError

    async def mass_send(self, messages: List[Sms]) -> List[int]:
        """
        Sending list of sms
        :param messages: list of Sms
        :return: Internal ids for checking status
        """
        raise NotImplementedError

    async def get_status(self, sms_id: int) -> SmsStatus:
        """ Retrieve single sms status by its' ids """
        raise NotImplementedError

    async def validate_account(self) -> bool:
        """ Return True if credentials valid, False otherwise """
        raise NotImplementedError

    async def save_message(self, message):
        pass
