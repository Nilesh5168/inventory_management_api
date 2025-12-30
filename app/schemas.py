from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import enum


class TransactionType(str, enum.Enum):
    IN = "IN"
    OUT = "OUT"


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    available_quantity: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class StockTransactionBase(BaseModel):
    product_id: int
    quantity: int
    transaction_type: TransactionType


class StockTransactionCreate(StockTransactionBase):
    pass


class StockTransaction(StockTransactionBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

from typing import List


class SupplierInfo(BaseModel):
    id: int
    name: str
    contact_email: str

    class Config:
        orm_mode = True


class LowStockAlert(BaseModel):
    product_id: int
    product_name: str
    sku: str
    warehouse_id: int
    warehouse_name: str
    current_stock: int
    threshold: int
    days_until_stockout: int
    supplier: SupplierInfo


class LowStockResponse(BaseModel):
    alerts: List[LowStockAlert]
    total_alerts: int
