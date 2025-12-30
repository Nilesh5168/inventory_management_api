from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/companies", tags=["Alerts"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{company_id}/alerts/low-stock", response_model=schemas.LowStockResponse)
def low_stock_alerts(company_id: int, db: Session = Depends(get_db)):

    alerts = []

    inventories = (
        db.query(models.Inventory)
        .join(models.Warehouse)
        .filter(models.Warehouse.company_id == company_id)
        .all()
    )

    for inv in inventories:
        product = inv.product
        if inv.quantity >= product.low_stock_threshold:
            continue

        supplier = product.suppliers[0] if product.suppliers else None

        alerts.append({
            "product_id": product.id,
            "product_name": product.name,
            "sku": product.sku,
            "warehouse_id": inv.warehouse.id,
            "warehouse_name": inv.warehouse.name,
            "current_stock": inv.quantity,
            "threshold": product.low_stock_threshold,
            "days_until_stockout": max(1, inv.quantity // 1),
            "supplier": supplier
        })

    return {
        "alerts": alerts,
        "total_alerts": len(alerts)
    }
