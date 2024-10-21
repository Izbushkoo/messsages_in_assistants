from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.util import await_only
from sqlmodel.ext.asyncio.session import AsyncSession

from app.api.deps import get_db_async
from app.models.database_models import Contact
from app.schemas.message import ContactTG, ContactTHR
from app.dals import messages_dals
from app.api import deps


router = APIRouter()


@router.post("/insert_contact")
async def insert_contact(contact: Contact, database: AsyncSession = Depends(get_db_async)):

    return await messages_dals.insert(contact, database)


@router.patch("/update_tg_nick")
async def update_tg_nick(contact: ContactTG, database: AsyncSession = Depends(get_db_async)):

    return await messages_dals.update_tg_nickname(contact_id=contact.contact_id, tg_nickname=contact.tg_nickname,
                                                  database=database)


@router.patch("/add_thread_to_contact")
async def add_thread_to_contact(contact: ContactTHR, database: AsyncSession = Depends(get_db_async)):
    return await messages_dals.add_new_thread_to_contact(contact_id=contact.contact_id, thread_id=contact.thread,
                                                  database=database)
