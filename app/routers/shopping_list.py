from fastapi import APIRouter

from app.db import data
from app.db.queries import get_list_by_id
from app.models import ShoppingList

router = APIRouter()


@router.get("/lists", response_model=list[ShoppingList])
def get_lists() -> list[ShoppingList]:
    return data["lists"]


@router.get("/lists/{list_id}", response_model=ShoppingList)
def get_list(list_id: int) -> ShoppingList:
    return get_list_by_id(list_id)
