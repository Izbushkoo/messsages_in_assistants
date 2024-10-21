from typing import Optional

from pydantic import BaseModel


class Contact(BaseModel):
    contact_id: str

class ContactTG(Contact):
    tg_nickname: Optional[str]

class ContactTHR(Contact):
    thread: Optional[str]
