import uuid
from datetime import datetime
from typing import Optional, List

from sqlalchemy import Column
from sqlmodel import SQLModel, Field, DateTime
from sqlalchemy.dialects.postgresql import JSON

def get_uuid():
    return str(uuid.uuid4())

class Contact(SQLModel, table=True):

    # id: Optional[str] = Field(default_factory=get_uuid, primary_key=True)

    contact_id: str = Field(primary_key=True)
    login_email: Optional[str] = Field(default=None, nullable=True)
    tg_nickname: Optional[str] = Field(nullable=True)

    threads: List[str] = Field(
        sa_column=Column(JSON, nullable=False)
    )




