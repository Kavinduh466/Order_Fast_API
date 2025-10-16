from fastapi import FastAPI
from database import engine
from database import SessionLocal
from models.order import Base
from routers.orderrouter import router


app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(router)


@app.get("/")
def greet():
    return "Hi"

