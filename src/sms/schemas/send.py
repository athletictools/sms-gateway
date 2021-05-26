from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    id: str = None
    phone_no: str
    text: str


class SendRequest(BaseModel):
    messages: List[Message]
