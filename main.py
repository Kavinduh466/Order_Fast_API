from fastapi import FastAPI
from database import engine
from database import SessionLocal
from routers.orderrouter import orderrouter
from routers.brandrouter import brandrouter

from models.base import Base
from models.order import Order, OrderItem
from models.brand import Brand, Product

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(orderrouter)
app.include_router(brandrouter)


@app.get("/")
def greet():
    return "Hi"

