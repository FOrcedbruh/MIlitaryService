from requests import Response
import requests
from aiogram.types import Message
import aiogram.utils.markdown as fmt
from settings import settings

class RequestsHelper():
    def get_orders(self) -> Response:
        res: Response = requests.get(url=settings.base_url + "orders/info")

        return res

    def get_last_order(self) -> Response:
        res: Response = requests.get(url=settings.base_url + "orders/last_order")

        return res
    
    def get_order_by_id(self, id: int) -> Response:
        res: Response = requests.get(url=settings.base_url + f"orders/get_order_by_id_for_bot/{id}")

        return res

    async def orders_response_form(
        self, order_number: str,
        address: str,
        delivery_type: str, 
        payment_type: str, 
        is_paid: str, 
        message: Message,
        cost_sum: int,
        customer_phone: str,
        customer_email: str,
        customer_name: str,
        created_at: str,
        products: str
    ):
        products_list: str = ""
        for i, product in enumerate(products):
            products_list += f"{i + 1}. {product}\n"

        created_at_date: str = created_at[:10].replace("-", ".")
        created_at_time: str = created_at[11:16]
        await message.answer(text=(
            fmt.text(
                fmt.text(fmt.hbold(f"Номер заказа: {order_number}")),
                fmt.text(fmt.hunderline(f"Адрес доставки: {address}")),
                fmt.text(f"Доставка: {delivery_type}"),
                fmt.text(f"Оплата: {payment_type}"),
                fmt.text(f"Статус оплаты: {"Оплачено" if is_paid == True else "Не оплачено"}"),
                fmt.text(f"Общая стоимость: {cost_sum}"),
                fmt.text(f"Телефон заказчика: {customer_phone}"),
                fmt.text(f"Почта заказчика: {customer_email}"),
                fmt.text(f"Имя заказчика: {customer_name}\n"),
                fmt.text(
                    fmt.text(fmt.hbold("Товары: \n")),
                    fmt.text(products_list),
                ),
                fmt.text(f"Заказ оформлен {created_at_date} в {created_at_time}"),
                sep="\n"
            )
        ), parse_mode="HTML")
        return
    
    def get_text_form_for_order(
        self, 
        order_number: str,
        address: str,
        delivery_type: str, 
        payment_type: str, 
        is_paid: str, 
        cost_sum: int,
        customer_phone: str,
        customer_email: str,
        customer_name: str,
        created_at: str,
        products: str
    ) -> str:
        products_list: str = ""
        for i, product in enumerate(products):
            products_list += f"{i + 1}. {product}\n"

        created_at_date: str = created_at[:10].replace("-", ".")
        created_at_time: str = created_at[11:16]
        return fmt.text(
                fmt.text(fmt.hbold(f"Номер заказа: {order_number}")),
                fmt.text(fmt.hunderline(f"Адрес доставки: {address}")),
                fmt.text(f"Доставка: {delivery_type}"),
                fmt.text(f"Оплата: {payment_type}"),
                fmt.text(f"Статус оплаты: {"Оплачено" if is_paid == True else "Не оплачено"}"),
                fmt.text(f"Общая стоимость: {cost_sum}"),
                fmt.text(f"Телефон заказчика: {customer_phone}"),
                fmt.text(f"Почта заказчика: {customer_email}"),
                fmt.text(f"Имя заказчика: {customer_name}\n"),
                fmt.text(
                    fmt.text(fmt.hbold("Товары: \n")),
                    fmt.text(products_list),
                ),
                fmt.text(f"Заказ оформлен {created_at_date} в {created_at_time}"),
                sep="\n"
            )
    
    def error_text_message(self, error_reason: str, status_code: int) -> str:
        return f"Ошибка: {str(status_code)} {error_reason}"
    
    async def error_response_form(
        self,
        message: Message,
        error_reason: str,
        status_code: int
    ):
        await message.answer(text=self.error_text_message(error_reason=error_reason, status_code=status_code))

    INACTIVE: str = "Сервер неактивен или упал ⚙️"


requestHelper = RequestsHelper()