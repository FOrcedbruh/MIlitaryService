from fastapi import APIRouter, Body, Depends
from dto.orders import OrderReadSchema, OrderCreateSchema, OrderReadSchemaAfterCreate
from services import OrderService
from dependencies import get_order_service

router = APIRouter(prefix="/orders", tags=["Orders"])



@router.get("/{order_id}", response_model=OrderReadSchema)
async def index(
    order_id: int,
    service: OrderService = Depends(get_order_service)
) -> OrderReadSchema:
    return await service.get_order(order_id)

@router.post("/", response_model=OrderReadSchemaAfterCreate)
async def index(
    order_in: OrderCreateSchema,
    service: OrderService = Depends(get_order_service)
) -> OrderReadSchemaAfterCreate:
    return await service.create_order(order_in)

@router.get("/", response_model=list[OrderReadSchema])
async def index(
    service: OrderService = Depends(get_order_service)
) -> list[OrderReadSchema]:
    return await service.get_orders()