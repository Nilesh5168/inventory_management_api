from fastapi import FastAPI
from app.routers import products, stock, alerts
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management API")

app.include_router(products.router)
app.include_router(stock.router)
app.include_router(alerts.router)
