from client.base_client import BaseClient

class AuthenticateClient(BaseClient):

    def login(self, payload):
        return self.post("/api/Authenticate/Login", json=payload)

    def get_auth_data(self):
        return self.get("/api/Authenticate/Get")