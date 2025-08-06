from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter(prefix="/stock", tags=["Stock"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.StockTransaction)
def create_transaction(tx: schemas.StockTransactionCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_stock_transaction(db, tx)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.StockTransaction])
def get_all_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@router.get("/product/{product_id}", response_model=list[schemas.StockTransaction])
def get_transactions_by_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_transactions_for_product(db, product_id)
