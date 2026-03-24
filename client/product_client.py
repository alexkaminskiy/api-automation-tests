from client.base_client import BaseClient

class ProductClient(BaseClient):

    def get_product(self, id):
        return self.get(f"/Product/GetProductById/{id}")

    def get_product_by_id_and_name(self, id=None, name=None):
        params = {}
        if id is not None: params["Id"] = id
        if name is not None: params["Name"] = name
        return self.get("/Product/GetProductByIdAndName", params=params)

    def get_product_by_name(self, name):
        return self.get(f"/Product/GetProductByName/{name}")

    def get_products(self):
        return self.get("/Product/GetProducts")

    def create_product(self, payload):
        return self.post("/Product/Create", json=payload)

    def upload_file(self, filepath):
        with open(filepath, "rb") as f:
            files = {"myFile": (filepath, f, "multipart/form-data")}
            return self.post("/Product", files=files)

    def download_file(self, filename):
        return self.get(f"/Product/{filename}")