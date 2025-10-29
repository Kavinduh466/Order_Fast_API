from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.brand import BrandCreate, BrandResponse
from services.brand_service import (
    create_brand,
    get_all_brands
)

brandrouter = APIRouter(prefix="/brands", tags=["Brands"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@brandrouter.post("/",response_model=BrandResponse)
def create_brand_route(brand_data: BrandCreate, db:Session = Depends(get_db)):
    return create_brand(db, brand_data)

@brandrouter.get("/", response_model=list[BrandResponse])
def get_all_brand_route(db: Session = Depends(get_db)):
    return get_all_brands(db)