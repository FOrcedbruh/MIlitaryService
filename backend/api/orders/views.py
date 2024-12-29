from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import db
from .schemas import OrderCreateSchema, OrderInfoReadSchema
from . import utils, crud
from .bot_api.crud import bot_crud
from .bot_api.utils import bot_utils

router = APIRouter(prefix="/orders", tags=["Orders"])



@router.post("/create")
async def index(
    session: AsyncSession = Depends(db.generate_session),
    order_in: OrderCreateSchema = Depends(utils.GetCreateItemData)
) -> dict:
    return await crud.create_order(session=session, order_in=order_in)


@router.get("/")
async def index(
    session: AsyncSession = Depends(db.generate_session)
):
    return await crud.get_orders(session=session)


@router.get("/info")
async def index(
    session: AsyncSession = Depends(db.generate_session)
):
    return await bot_crud.get_orders_for_info(session=session)


@router.get("/last_order", response_model=OrderInfoReadSchema)
async def index(
    session: AsyncSession = Depends(db.generate_session)
) -> OrderInfoReadSchema:
    return await bot_crud.get_last_order(session=session)


@router.get("/{order_id}", response_model_exclude_none=True)
async def index(
    order_id: int,
    session: AsyncSession = Depends(db.generate_session)
):
    return await crud.get_order(session=session, order_id=order_id)

@router.post("/test_send_new_order")
async def index(
    order_number: str,
    order_id: int
):
    return await bot_utils.send_new_order_to_bot(order_id=order_id, order_number=order_number)

@router.get("/get_order_by_id_for_bot/{order_id}")
async def index(
    order_id: int,
    session: AsyncSession = Depends(db.generate_session)
):
    return await bot_crud.get_order_for_bot_by_id(order_id=order_id, session=session)