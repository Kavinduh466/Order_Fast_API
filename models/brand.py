
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime,timezone
import enum
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

Base = declarative_base()

class ProductTypeEnum(str, enum.Enum):
    Clothes = "CLOTHES"
    Electronic = "ELECTRONIC"
    HandCraft = "HANDCRAFT"
    Toys = "TOYS"

class Product(Base):
        __tablename__ = "products"

        product_id  = Column(Integer, primary_key=True, index=True)
        productType = Column(Enum(ProductTypeEnum), default=ProductTypeEnum.Electronic)
        productName = Column(String, nullable= False)
        price = Column(Integer, nullable=False)

        brand_id = Column(Integer, ForeignKey("brands.brand_id"))

        brand = relationship("Brand", back_populates="products")

        

class Brand(Base):
    __tablename__ = "brands"

    brand_id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String, unique=True, nullable=False)
    country = Column(String, nullable=True)
    website = Column(String, nullable=True)

    products = relationship("Product", back_populates="brand")

