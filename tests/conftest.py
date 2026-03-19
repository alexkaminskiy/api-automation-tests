import allure
import pytest

from src.config_loader import load_config
from src.api_client import APIClient


@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture(scope="session")
def client(config):
    client = APIClient(base_url=config.get("base_url"), timeout=config.get("timeout", 10))
    yield client
    try:
        client.session.close()
    except Exception:
        pass


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        client = item.funcargs.get("client")
        if client and getattr(client, "last_response", None) is not None:
            resp = client.last_response
            try:
                content = resp.text
                allure.attach(content, name="response", attachment_type=allure.attachment_type.JSON)
            except Exception:
                try:
                    allure.attach(resp.content, name="response", attachment_type=allure.attachment_type.BINARY)
                except Exception:
                    pass
