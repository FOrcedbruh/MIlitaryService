import requests
from requests import Response
from schemas import OrderSchema

class RequestsHelper():
    async def get_orders() -> Response:
        res: Response = await  requests.get(url="http://127.0.0.1:7979/api/orders/")

        return res

    def get_last_order() -> OrderSchema:
        pass


requestHelper = RequestsHelper()