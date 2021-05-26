import pytest
from fastapi.testclient import TestClient

from sms.handlers import app


@pytest.fixture
def http_client() -> TestClient:
    return TestClient(app)
