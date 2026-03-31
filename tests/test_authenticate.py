import pytest
import allure
from client.authenticate_client import AuthenticateClient
from utils.faker_factory import fake_login


@pytest.fixture
def client():
    return AuthenticateClient()

@pytest.mark.smoke
def test_fake_login_success(client):

    with allure.step("Allure Get fake login data and send login request"):
        payload = fake_login()
        r = client.login(payload)
    
    with allure.step("Validate response status and body"):

        assert r.status_code == 200
        assert r.json().get("token") is not None
        assert r.json().get("message") == "Success"

def test_get_auth_data(client):
    r = client.get_auth_data()
    with allure.step("Validate response status"):
        assert r.status_code == 200