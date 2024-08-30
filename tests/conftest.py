import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


# para não ficar repetindo
@pytest.fixture
def client():
    return TestClient(app)
