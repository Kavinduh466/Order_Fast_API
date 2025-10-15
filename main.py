from fastapi import FastAPI
from database_config import engine
from database_config import SessionLocal
from models.order import Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hi"