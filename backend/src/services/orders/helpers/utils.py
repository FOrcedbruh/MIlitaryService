from dto.orders import OrderCreateSchema
import random


def generate_order_number(order_in: OrderCreateSchema) -> str:
    code: str = ""
    for _ in range(5):
        code += str(random.randrange(0, 9))
    vals_str: str = ""
    for v in order_in.model_dump(exclude_none=True).values():
        vals_str += str(v)
    code += str(len(vals_str.encode()))

    return code