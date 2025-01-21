from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



def main_keyboard() -> ReplyKeyboardMarkup:
    kb_list: list = [
        [KeyboardButton(text="Посмотреть все заказы"), KeyboardButton(text="Посмотреть подробности заказа")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return keyboard

def order_numbers_keyboard(orders: list[str]) -> ReplyKeyboardMarkup:
    kb_list: list = []
    for order in orders:
        kb_list.append([KeyboardButton(text=order)])
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return keyboard