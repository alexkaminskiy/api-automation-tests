from typing import Optional, List
from pydantic import BaseModel

class LoginModel(BaseModel):
    userName: str
    password: str

class Components(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    productId: Optional[int]
    product: Optional["Product"] = None

class Product(BaseModel):
    productId: Optional[int]
    name: Optional[str]
    description: Optional[str]
    price: Optional[int]
    components: Optional[List[Components]] = None
    productType: Optional[int]

Components.update_forward_refs()