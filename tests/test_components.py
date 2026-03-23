import pytest
from utils.faker_factory import fake_component


def test_get_component_by_product_id(client):
    r = client.get_component_by_product_id(1)

    assert r.status_code == 200

def test_get_components_by_product_id(client):
    r = client.get_components_by_product_id(1)

    assert r.status_code == 200

def test_create_component(client):
    payload = fake_component(product_id=1)
    r = client.create_component(payload)

    assert r.status_code == 200