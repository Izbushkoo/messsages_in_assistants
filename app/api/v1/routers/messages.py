from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.api.deps import get_db_async
from app.models.database_models import Message
from app.api import deps


router = APIRouter()


@router.post("/insert")
async def insert_message(message: Message, database: AsyncSession = Depends(get_db_async)):
