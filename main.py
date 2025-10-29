from fastapi import FastAPI
from database import engine
from database import SessionLocal
from models.order import Base
from routers.orderrouter import orderrouter
from routers.brandrouter import brandrouter

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(orderrouter)
app.include_router(brandrouter)


@app.get("/")
def greet():
    return "Hi"

