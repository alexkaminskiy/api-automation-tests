import pytest
from utils.faker_factory import fake_product


def test_get_product(client):
    r = client.get_product(1)
    assert r.status_code in (200, 404)

def test_get_products(client):
    r = client.get_products()
    assert r.status_code == 200

def test_create_product(client):
    payload = fake_product()
    r = client.create_product(payload)
    assert r.status_code in (200, 400)