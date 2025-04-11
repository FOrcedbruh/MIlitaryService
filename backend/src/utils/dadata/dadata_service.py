from ..base_service import BaseApiService
from httpx import AsyncClient, Response
from core.config import settings
from typing import Any


class DadataService(BaseApiService):
    base_url: str = settings.dadatacfg.base_url
    secret_key: str = ""
    api_key: str = "a6ab205da9f35313df263981149ed1e3b174f23d"
    suggest_limit: int = 10

    async def __aenter__(self):
        self.client = AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Token {self.api_key}"}
        )
        return self
    
    async def __aexit__(self, *args):
        await self.client.aclose()
    
    async def suggest_address(self, data: str, limit: int = suggest_limit) -> list[dict[str, Any]]:
        res: Response = await self.client.post(url="/suggest/address", json={
            "query": data,
            "count": limit
        })
        res_data = res.json()
        return res_data.get("suggestions", None)