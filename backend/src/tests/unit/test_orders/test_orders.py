import pytest
from httpx import AsyncClient
from fastapi import status


class TestOrders:

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "id, status_code",
        [
            (16, status.HTTP_200_OK),
            (17, status.HTTP_200_OK),
            (9999, status.HTTP_400_BAD_REQUEST)
        ]
    )
    async def test_get_order_by_id(
        self, 
        id: int,
        status_code: int,
        async_client: AsyncClient
    ):
        res = await async_client.get(f"/orders/{id}")
        assert res.status_code == status_code


    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "number, status_code",
        [
            ("12345678", status.HTTP_200_OK),
            ("3421565", status.HTTP_200_OK),
            ("notexists", status.HTTP_400_BAD_REQUEST)
        ]
    )
    async def test_get_order_by_number(
        self, 
        number: str,
        status_code: int,
        async_client: AsyncClient
    ):
        res = await async_client.get(f"/orders/by_number?order_number={number}")
        assert res.status_code == status_code


    @pytest.mark.asyncio
    async def test_get_numbers(
        self, 
        async_client: AsyncClient
    ):
        res = await async_client.get("/orders/numbers")
        assert res.status_code == status.HTTP_200_OK