from ..AbstractClient.AbstractClient import AbstractClient
from dto.orders import OrderReadSchema
from ..utils.retry import retry
import httpx
from httpx import Response
from core import logger

class StoreClient(AbstractClient):

    def __init__(self, url: str):
        self.url = url

    @retry(times=6, sleep_secs=2)
    def get_all(self, endpoint: str) -> list[OrderReadSchema]:
        res: Response = httpx.get(url=self.url+endpoint)
        logger.info(f"Ответ: {res.status_code} от {res._request.method} {self.url+endpoint}")
        return res.json()
    
    @retry(times=6, sleep_secs=2)
    async def get_one(self, endpoint: str) -> OrderReadSchema:
        res: Response = httpx.get(url=self.url+endpoint)
        logger.info(f"Ответ: {res.status_code} от {res._request.method} {self.url+endpoint}")
        return res.json()
    

    