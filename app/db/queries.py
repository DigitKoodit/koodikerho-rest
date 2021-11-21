from fastapi import HTTPException

from app.db import data
from app.models import Product, ShoppingList


def get_product_from_list_by_id(list_id: int, product_id: int) -> Product:
    for shopping_list in data["lists"]:
        if shopping_list["id"] == list_id:
            for product in shopping_list["products"]:
                if product["id"] == product_id:
                    return Product.parse_obj(product)
    raise HTTPException(status_code=404, detail="Product not found")


def update_product_from_list_by_id(
    list_id: int, product_id: int, new_product: Product
) -> Product:
    for shopping_list in data["lists"]:
        if shopping_list["id"] == list_id:
            for i, product in enumerate(shopping_list["products"]):
                if product["id"] == product_id:
                    product["name"] = new_product.name
                    product["quantity"] = new_product.quantity
                    return Product.parse_obj(product)
    raise HTTPException(status_code=404, detail="Product not found")


def delete_product_from_list_by_id(list_id: int, product_id: int) -> None:
    for shopping_list in data["lists"]:
        if shopping_list["id"] == list_id:
            for i, product in enumerate(shopping_list["products"]):
                if product["id"] == product_id:
                    shopping_list["products"].pop(i)
                    return
    raise HTTPException(status_code=404, detail="Product not found")


def get_list_by_id(list_id: int) -> ShoppingList:
    for shopping_list in data["lists"]:
        if shopping_list["id"] == list_id:
            return ShoppingList.parse_obj(shopping_list)
    raise HTTPException(status_code=404, detail="List not found")
