from fastapi import FastAPI
from app.routers import products, stock
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management API")

# ✅ Add a root path to avoid 404 at /
@app.get("/")
def root():
    return {"message": "Welcome to the Inventory Management API"}

# Include routers
app.include_router(products.router)
app.include_router(stock.router)
