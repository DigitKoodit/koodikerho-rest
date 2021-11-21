from fastapi import FastAPI

from app.routers import product, shopping_list

app = FastAPI()
app.include_router(product.router)
app.include_router(shopping_list.router)
