from sqlalchemy.orm import Session
from app import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session):
    return db.query(models.Product).all()

def update_product(db: Session, product_id: int, product_data: schemas.ProductUpdate):
    product = get_product(db, product_id)
    for key, value in product_data.dict().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    db.delete(product)
    db.commit()

def create_stock_transaction(db: Session, tx: schemas.StockTransactionCreate):
    product = get_product(db, tx.product_id)
    if not product:
        return None
    if tx.transaction_type == "IN":
        product.available_quantity += tx.quantity
    elif tx.transaction_type == "OUT":
        if product.available_quantity < tx.quantity:
            raise ValueError("Insufficient stock.")
        product.available_quantity -= tx.quantity

    db_tx = models.StockTransaction(**tx.dict())
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx

def get_transactions(db: Session):
    return db.query(models.StockTransaction).all()

def get_transactions_for_product(db: Session, product_id: int):
    return db.query(models.StockTransaction).filter(models.StockTransaction.product_id == product_id).all()
