
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime,timezone
import enum
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

Base = declarative_base()  # tells this class is modal and wants to map 


class Product(Base):
    __tablename__ = "product"

    prodcutId = Column(Integer, primary_key=True, index=True)
    productName = Column(String, nullable=False)
    description = Column(String, nullable=True)
    sku = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

