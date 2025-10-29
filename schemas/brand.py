from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from enum import Enum


class ProductTypeEnum(str, Enum):
    Clothes = "CLOTHES"
    Electronic = "ELECTRONIC"
    HandCraft = "HANDCRAFT"
    Toys = "TOYS"


class ProductItemCreate(BaseModel):
    product_id: int
    productType: str
    productName: str
    

class BrandCreate(BaseModel):
    brand_id: int 
    brand_name: str
    country: str
    website: str
    products: List[ProductItemCreate]

class ProductItemResponse(BaseModel):
    product_id: int
    product_name: str
    product_type: str
    price: int

class BrandResponse(BaseModel):
    brand_id : int
    brand_name: str
    country: str
    website: str
    products: List[ProductItemResponse]

    class Config:
        orm_mode = True