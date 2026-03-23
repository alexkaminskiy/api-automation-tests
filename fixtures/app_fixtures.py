import pytest
from client.authenticate_client import AuthenticateClient
from client.components_client import ComponentsClient
from client.product_client import ProductClient

@pytest.fixture
def client():
    return AuthenticateClient()

@pytest.fixture
def client():
    return ComponentsClient()

@pytest.fixture
def client():
    return ProductClient()