from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import db
from .schemas import OrderCreateSchema, OrderReadSchema
from . import utils, crud



router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/create")
async def index(
    session: AsyncSession = Depends(db.generate_session),
    order_in: OrderCreateSchema = Depends(utils.GetCreateItemData)
) -> dict:
    return await crud.create_order(session=session, order_in=order_in)


@router.get("/{order_id}", response_model_exclude_none=True)
async def index(
    order_id: int,
    session: AsyncSession = Depends(db.generate_session)
) -> OrderReadSchema:
    return await crud.get_order(session=session, order_id=order_id)