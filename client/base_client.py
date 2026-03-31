import requests
import logging
import sys
from typing import Optional
from config.settings import BASE_URL, AUTH_USER, AUTH_PASSWORD
from utils.logger import get_logger
from utils.helper import sanitize_data


logger = get_logger()


class BaseClient:
    def __init__(self, base_url: Optional[str] = BASE_URL, token: Optional[str] = None, timeout: int = 10):
        self.base_url = base_url.rstrip("/") if base_url else ""
        self.timeout = timeout
        self.session = requests.Session()
        self.last_response = None

        logger.info(f"Initializing BaseClient with base_url={self.base_url}")
        self.token = token if token else self._get_token()

    @property
    def headers(self) -> dict:
        h = {"Content-Type": "application/json"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

    def _get_token(self) -> str:
        auth_url = self._build_url('/api/Authenticate/Login')
        logger.info(f"Requesting auth token from {auth_url}")
        
        r = requests.post(auth_url, json={"username": AUTH_USER, "password": AUTH_PASSWORD})

        logger.debug(f"Auth response status={r.status_code}")

        r.raise_for_status()
        token = r.json().get("token")

        logger.info("Token successfully retrieved")
        
        return token

    def _build_url(self, path: str) -> str:
        if path.startswith("http://") or path.startswith("https://"):
            logger.debug(f"Using absolute URL: {path}")
            return path

        full_url = f"{self.base_url}/{path.lstrip('/')}"
        logger.debug(f"Built URL: {full_url}")
        return full_url

    def mask_sensitive(self, data: dict) -> dict:
        safe = data.copy()
        if "Authorization" in safe:
            token = safe["Authorization"]
            if isinstance(token, str) and len(token) > 10:
                safe["Authorization"] = token[:10] + "...***MASKED***"
            else:
                safe["Authorization"] = "***MASKED***"
        return safe

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = self._build_url(path)
        kwargs.setdefault("timeout", self.timeout)

        logger.info(f"Sending {method.upper()} request to {url}")
        
        # Masked headers for logging

        safe_headers = self.mask_sensitive(self.headers)
        logger.debug(f"Request headers: {safe_headers}")

        if "json" in kwargs:
            logger.debug(f"Payload: {kwargs.get('json')}")
        if "params" in kwargs:
            logger.debug(f"Query params: {kwargs.get('params')}")

        resp = self.session.request(method, url, headers=self.headers, **kwargs)
        self.last_response = resp

        logger.info(f"Response {resp.status_code} from {url}")

        safe_text = sanitize_data(resp.text)
        logger.debug(f"Response body: {safe_text}")
        # logger.debug(f"Response body: {resp.text}")

        return resp

    def get(self, path: str, params: Optional[dict] = None, **kwargs) -> requests.Response:
        return self.request("GET", path, params=params, **kwargs)

    def post(self, path: str, json: Optional[dict] = None, files: Optional[dict] = None, **kwargs) -> requests.Response:
        return self.request("POST", path, json=json, files=files, **kwargs)

    def put(self, path: str, json: Optional[dict] = None, **kwargs) -> requests.Response:
        return self.request("PUT", path, json=json, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.request("DELETE", path, **kwargs)
    