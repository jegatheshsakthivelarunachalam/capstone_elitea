from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.config import APP_NAME, APP_ENV

app = FastAPI(
    title=APP_NAME,
    description="A sample inventory API for the EliteA documentation workflow.",
    version="1.0.0",
)

class Product(BaseModel):
    id: int
    name: str
    category: str
    in_stock: bool

PRODUCTS = [
    Product(id=1, name="Wireless Mouse", category="Accessories", in_stock=True),
    Product(id=2, name="USB-C Hub", category="Accessories", in_stock=True),
    Product(id=3, name="Laptop Stand", category="Workspace", in_stock=False),
]

@app.get("/health", tags=["Operations"])
def health():
    return {"status": "healthy", "environment": APP_ENV}

@app.get("/products", response_model=list[Product], tags=["Products"])
def list_products():
    return PRODUCTS

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product(product_id: int):
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
