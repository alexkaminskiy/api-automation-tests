from client.base_client import BaseClient

class ComponentsClient(BaseClient):

    def get_component_by_product_id(self, id):
        return self.get(f"/Components/GetComponentByProductId/{id}")

    def get_components_by_product_id(self, id):
        return self.get(f"/Components/GetComponentsByProductId/{id}")

    def create_component(self, payload):
        return self.post("/Components/CreateComponent", json=payload)

    def get_all_components(self):
        return self.get("/Components/GetAllComponents")