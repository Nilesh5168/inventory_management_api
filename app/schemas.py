from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import enum

class TransactionType(str, enum.Enum):
    IN = "IN"
    OUT = "OUT"

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = ""
    price: float
    available_quantity: int

class ProductCreate(ProductBase): pass
class ProductUpdate(ProductBase): pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class StockTransactionBase(BaseModel):
    product_id: int
    quantity: int
    transaction_type: TransactionType

class StockTransactionCreate(StockTransactionBase): pass

class StockTransaction(StockTransactionBase):
    id: int
    timestamp: datetime
    class Config:
        orm_mode = True
