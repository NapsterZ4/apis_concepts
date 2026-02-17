from fastapi import FastAPI
from endpoints import users, products

app = FastAPI(
    title="APIs creation class",
    version="0.0.1"
)

app.include_router(users.router, prefix="/api/v3")
app.include_router(products.router, prefix="/api/v2")
