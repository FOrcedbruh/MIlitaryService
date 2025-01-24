from aiogram.utils.formatting import (
    Bold, as_list, as_key_value, as_marked_section, Text, HashTag
)
from dto.orders import OrderReadSchema
from datetime import datetime


class OrderFormatting():
    
    def get_content(self, order: OrderReadSchema) -> Text:
        content = as_list(
            Bold("ℹ️ Подробности заказа"),
            as_marked_section(
                Bold("Заказчик 👤"),
                as_key_value("Номер заказа", order["order_number"]),
                as_key_value("Заказчик", order["customer_name"]),
                as_key_value("Почта заказчика", order["customer_email"]),
                as_key_value("Телефон", order["customer_phone"]),
                as_key_value("Статус оплаты", "Оплачен" if order["is_paid"] else "Не оплачен"),
            ),
            as_marked_section(
                Bold("Информация о заказе"),
                as_key_value("Сумма заказа", f"{str(order["cost_sum"])} руб."),
                as_key_value("Тип оплаты", order["payment_type"]),
                as_key_value("Тип получения заказа", order["delivery_type"]),
                as_key_value("Адрес доставки", order["address"]),
                as_key_value("Товары", as_list(order["products"]))
            ),
            as_marked_section(
                Bold(" "),
                as_key_value("Дата оформления заказа", self.format_date(order["created_at"])),
                marker="🕰 ",
            ),
            HashTag("#заказы"),
            sep="\n\n",
        )
        return content

    def format_date(self, date: datetime) -> str:
        return str(date)[:10].replace("-", ".") + " года" + " в " + str(date)[11:16]


    