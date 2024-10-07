from httpx import AsyncClient, ASGITransport
from pytest_asyncio import fixture

from app.main import app


@fixture(scope="function")
async def async_client():
    ac = AsyncClient(transport=ASGITransport(app=app), base_url='http://test')
    try:
        yield ac
    finally:
        await ac.aclose()

