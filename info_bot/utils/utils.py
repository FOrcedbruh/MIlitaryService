from requests import Response
from api import requestHelper
from schemas.schemas import OrderInfoReadSchema
from aiogram.types import Message, CallbackQuery

async def get_all_orders(message: Message):
    try:
        orders: Response = requestHelper.get_orders()
        orders_json: list[OrderInfoReadSchema] = orders.json()
        if (orders.status_code != 200):
            await requestHelper.error_response_form(message=message, error_reason=orders.reason, status_code=orders.status_code)
            return
        await message.answer(text="Вот все текущие и завершенные заказы 📦")
        for order_json in orders_json:
            await requestHelper.orders_response_form(**order_json, message=message)
        return
    except Exception:
        await message.answer(text=requestHelper.INACTIVE)

async def get_last_order(message: Message):
    try:
        order: Response = requestHelper.get_last_order()
        if (order.status_code != 200):
            await requestHelper.error_response_form(message=message, error_reason=order.reason, status_code=order.status_code)
            return
        order_json = order.json()
        await message.answer(text="Последний оформленный заказ ⏳")
        await requestHelper.orders_response_form(**order_json, message=message)
        return
    except Exception:
        await message.answer(text=requestHelper.INACTIVE)

async def get_order_by_id(order_id: int, order_number: str):
    order: Response = requestHelper.get_order_by_id(id=order_id)
    return order.json()