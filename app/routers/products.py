from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from decimal import Decimal
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/products", tags=["Products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Product)
def create_product(payload: schemas.ProductCreate, db: Session = Depends(get_db)):

    if db.query(models.Product).filter_by(sku=payload.sku).first():
        raise HTTPException(status_code=400, detail="SKU already exists")

    warehouse = db.query(models.Warehouse).filter_by(id=payload.warehouse_id).first()
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")

    try:
        product = models.Product(
            name=payload.name,
            sku=payload.sku,
            price=Decimal(payload.price)
        )
        db.add(product)
        db.flush()

        inventory = models.Inventory(
            product_id=product.id,
            warehouse_id=payload.warehouse_id,
            quantity=payload.initial_quantity
        )
        db.add(inventory)

        db.commit()
        return product

    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create product")
