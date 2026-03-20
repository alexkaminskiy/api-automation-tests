import pytest
from client.components_client import ComponentsClient
from utils.faker_factory import fake_component

@pytest.fixture
def client():
    return ComponentsClient()

def test_get_component_by_product_id(client):
    r = client.get_component_by_product_id(1)
    assert r.status_code in (200, 404)

def test_get_components_by_product_id(client):
    r = client.get_components_by_product_id(1)
    assert r.status_code in (200, 404)

def test_create_component(client):
    payload = fake_component(product_id=1)
    r = client.create_component(payload)
    assert r.status_code in (200, 400)