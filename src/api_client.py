import requests
from typing import Optional


class APIClient:
    def __init__(self, base_url: Optional[str] = None, timeout: int = 10):
        self.base_url = base_url.rstrip("/") if base_url else ""
        self.timeout = timeout
        self.session = requests.Session()
        self.last_response = None

    def _build_url(self, path: str) -> str:
        if path.startswith("http://") or path.startswith("https://"):
            return path
        return f"{self.base_url}/{path.lstrip('/')}" if self.base_url else path

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = self._build_url(path)
        kwargs.setdefault("timeout", self.timeout)
        resp = self.session.request(method, url, **kwargs)
        self.last_response = resp
        return resp

    def get(self, path: str, params: dict = None, **kwargs) -> requests.Response:
        return self.request("GET", path, params=params, **kwargs)

    def post(self, path: str, json: dict = None, data: dict = None, **kwargs) -> requests.Response:
        return self.request("POST", path, json=json, data=data, **kwargs)

    def put(self, path: str, json: dict = None, **kwargs) -> requests.Response:
        return self.request("PUT", path, json=json, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.request("DELETE", path, **kwargs)
