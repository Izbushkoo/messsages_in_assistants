import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, DateTime

def get_uuid():
    return str(uuid.uuid4())

class Message(SQLModel, table=True):

    id: Optional[str] = Field(default_factory=get_uuid, primary_key=True)
    created_at: Optional[str] = Field(default_factory=datetime.now, sa_column_kwargs={"default": DateTime})

    service_name: str = Field(nullable=False)
    tg_nickname: Optional[str] = Field(nullable=False)

    role: Optional[str] = Field(nullable=True)
    content: Optional[str] = Field(nullable=True)
