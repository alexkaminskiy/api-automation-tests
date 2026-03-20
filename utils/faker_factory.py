from faker import Faker
fake = Faker()

def fake_login():
    return {
        "userName": fake.user_name(),
        "password": fake.password()
    }

def fake_product():
    return {
        "productId": 0,
        "name": fake.word(),
        "description": fake.text(max_nb_chars=40),
        "price": fake.random_int(10, 500),
        "components": None,
        "productType": fake.random_int(0, 5),
    }

def fake_component(product_id=None):
    return {
        "id": 0,
        "name": fake.word(),
        "description": fake.text(40),
        "productId": product_id,
        "product": None,
    }