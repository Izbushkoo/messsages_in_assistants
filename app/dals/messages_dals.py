from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.database_models import Message


async def insert_message(message: Message, database: AsyncSession):

    async with database as session:


