import pytest
from aiohttp.test_utils import TestClient
from sms.application import app_factory


@pytest.fixture
async def http_client(aiohttp_client, loop) -> TestClient:
    app = await app_factory()
    client = await aiohttp_client(app)
    return client
