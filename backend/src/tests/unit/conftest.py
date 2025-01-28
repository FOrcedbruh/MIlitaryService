import pytest_asyncio
from httpx import AsyncClient
from core.config import settings



@pytest_asyncio.fixture(autouse=True)
async def async_client():
    async with AsyncClient(base_url=f"http://localhost:{settings.runcfg.port}/api/v1") as client:
        yield client


