# models/order.py

from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime,timezone
import enum
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

Base = declarative_base()

# -----------------------------
# SQLAlchemy Models
# -----------------------------

class OrderStatusEnum(str, enum.Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    user_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    shipping_address = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.PENDING)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_items"

    item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id", ondelete="CASCADE"))
    product_id = Column(Integer, nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_unit = Column(Float, nullable=False)

    order = relationship("Order", back_populates="items")


# -----------------------------
# Pydantic Models (DTOs)
# -----------------------------

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderCreate(BaseModel):
    user_id: int
    shipping_address: str
    items: List[OrderItemCreate]

class OrderItemResponse(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price_per_unit: float

class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    user_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    shipping_address: str
    items: List[OrderItemResponse]
    total_amount: float
    status: OrderStatusEnum
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
