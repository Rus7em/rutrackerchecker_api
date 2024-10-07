import pytest
from httpx import AsyncClient

from tests.fixtures import async_client


@pytest.mark.asyncio
async def test_api_find(async_client: AsyncClient):
    response = await async_client.post('/find/')
    assert response.status_code == 200
    result = response.json()
    assert result == True

