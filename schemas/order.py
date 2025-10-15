# app/schemas/order.py

from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Enum for order status
class OrderStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

# -----------------------------
# Request models
# -----------------------------

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderCreate(BaseModel):
    user_id: int
    shipping_address: str
    items: List[OrderItemCreate]

# -----------------------------
# Response models
# -----------------------------

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
    status: OrderStatus
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
