
class Sms:
    def __init__(self, phone_no: str, text: str):
        self.phone_no = phone_no
        self.text = text


class SmsStatus(Enum):
    sent = 1
    delivered = 2
    not_delivered = 3
