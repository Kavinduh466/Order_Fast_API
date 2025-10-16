from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderCreate(BaseModel):
    user_id: int
    shipping_address: str
    items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    shipping_address: Optional[str] = None
    status: Optional[OrderStatus] = None
    notes: Optional[str] = None

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
