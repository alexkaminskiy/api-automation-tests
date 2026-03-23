import pytest
from client.authenticate_client import AuthenticateClient
from utils.faker_factory import fake_login

@pytest.fixture
def client():
    return AuthenticateClient()

@pytest.mark.smoke
def test_login_success(client):
    payload = fake_login()
    r = client.login(payload)
    
    assert r.status_code == 200
    assert r.json().get("token") is not None
    assert r.json().get("message") == "Success"

def test_get_auth_data(client):
    r = client.get_auth_data()
    assert r.status_code == 200