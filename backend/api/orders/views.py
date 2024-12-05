from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import db
from .schemas import OrderCreateSchema
from . import utils, crud



router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/create")
async def index(
    session: AsyncSession = Depends(db.generate_session),
    order_in: OrderCreateSchema = Depends(utils.GetCreateItemData)
):
    return await crud.create_order(session=session, order_in=order_in)