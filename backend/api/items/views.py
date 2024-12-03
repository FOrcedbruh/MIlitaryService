from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import db
from .schemas import ItemCreateSchema
from . import utils, crud

router = APIRouter(prefix="/items", tags=["Items"])



@router.post("/add")
async def index(
    session: AsyncSession = Depends(db.generate_session),
    item_in: ItemCreateSchema = Depends(utils.GetCreateItemData)
):
    return await crud.create_item(session=session, item_in=item_in)