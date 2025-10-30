from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.brand import BrandCreate, BrandResponse, BrandUpdate
from services.brand_service import (
    create_brand,
    get_all_brands,
    get_brand_by_id_service,
    update_brand_by_id_service,
    delete_brand_by_id_service
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

@brandrouter.get("/{brand_id}", response_model=BrandResponse)
def get_brand_by_id(brand_id: int,db: Session = Depends(get_db)):
    return get_brand_by_id_service(db, brand_id)

@brandrouter.put("/{brand_id}", response_model=BrandResponse)
def update_brand_by_id(brand_id: int,brand_data: BrandUpdate, db: Session= Depends(get_db)):
    return update_brand_by_id_service(db, brand_id, brand_data)

@brandrouter.delete("/{brand_id}")
def delete_brand_by_id(brand_id:int, db:Session=Depends(get_db)):
    if(delete_brand_by_id_service(db, brand_id)):
        return "brand {brand_id}delted successfully"
