from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

class ProductUpdate(BaseModel):
    name: str
    price: float
    quantity: int

class ProductPatch(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    description: Optional[str] = None