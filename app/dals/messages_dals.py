from sqlmodel import select
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.database_models import Contact


async def insert(contact: Contact, database: AsyncSession):

    try:
        async with database as session:
            statement_to_select = select(Contact).where(Contact.contact_id == contact.contact_id)
            result = await session.exec(statement_to_select)
            if result:
                return result.first()
            else:
                session.add(contact)
                await session.commit()
                return contact
    except Exception as err:
        raise HTTPException(detail=f"Smth went wrong: {err}", status_code=500)


async def update_tg_nickname(contact_id: str, tg_nickname: str, database: AsyncSession):
    try:
        async with database as session:
            st = select(Contact).where(Contact.contact_id == contact_id)
            result = await session.exec(st)
            if result:
                contact = result.first()
                contact.tg_nickname = tg_nickname
                session.add(contact)
                await session.commit()
                await session.refresh(contact)
                return contact
    except Exception as err:
        raise HTTPException(detail=f"Smth went wrong: {err}", status_code=500)


async def add_new_thread_to_contact(contact_id: str, thread_id: str, database: AsyncSession):
    try:
        async with database as session:
            st = select(Contact).where(Contact.contact_id == contact_id)
            result = await session.exec(st)
            if result:
                contact = result.first()
                contact.threads.append(thread_id)
                session.add(contact)
                await session.commit()
                await session.refresh(contact)
                return contact
    except Exception as err:
        raise HTTPException(detail=f"Smth went wrong: {err}", status_code=500)




