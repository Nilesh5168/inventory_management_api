from pydantic import BaseModel, Field
from typing import Optional, List
from decimal import Decimal


class ProductCreate(BaseModel):
    name: str
    sku: str
    price: Decimal
    warehouse_id: int
    initial_quantity: int = Field(ge=0)


class Product(BaseModel):
    id: int
    name: str
    sku: str
    price: Decimal

    class Config:
        orm_mode = True


class SupplierOut(BaseModel):
    id: int
    name: str
    contact_email: str


class LowStockAlert(BaseModel):
    product_id: int
    product_name: str
    sku: str
    warehouse_id: int
    warehouse_name: str
    current_stock: int
    threshold: int
    days_until_stockout: int
    supplier: Optional[SupplierOut]


class LowStockResponse(BaseModel):
    alerts: List[LowStockAlert]
    total_alerts: int
