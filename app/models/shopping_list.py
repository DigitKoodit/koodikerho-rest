from pydantic import BaseModel

from app.models.product import Product


class ShoppingList(BaseModel):
    id: int
    name: str
    products: list[Product]
