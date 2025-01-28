import pytest
import pytest_asyncio
from httpx import AsyncClient
from fastapi import status
import asyncio


@pytest_asyncio.fixture(scope="session")
async def product_to_delete_id():
    return {
        "id": 0
    }



class TestProducts:
   
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "id, res",
        [
            (1, status.HTTP_200_OK),
            (2, status.HTTP_400_BAD_REQUEST)
        ]
    )
    async def test_get_product_by_id(
        self,
        async_client: AsyncClient,
        id: int,
        res
    ):
        response = await async_client.get(url=f"/products/{id}")
        assert response.status_code == res

    
    @pytest.mark.asyncio
    async def test_create_product(
        self,
        product_to_delete_id,
        async_client: AsyncClient
    ):
        product_to_create: dict = {
            "name": "Test product name",
            "description": "Test product desc",
            "limit": 100,
            "cost": 9990
        }
        res = await async_client.post(url="/products/", json=product_to_create)
        product_to_delete_id["id"] = res.json()["id"]
        assert res.status_code == status.HTTP_200_OK
    

    @pytest.mark.asyncio
    async def test_delete_product_by_id(
        self, 
        async_client: AsyncClient,
        product_to_delete_id,
    ):
        res = await async_client.delete(url=f"/products/{product_to_delete_id["id"]}")
        assert res.status_code == status.HTTP_200_OK

    @pytest.mark.asyncio
    async def test_get_products(
        self, 
        async_client: AsyncClient
    ):
        res = await async_client.get("/products/")
        assert res.status_code == status.HTTP_200_OK