from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.order import OrderCreate, OrderResponse, OrderUpdate
from services.order_service import (
    create_new_order,
    get_orders,
    get_order,
    update_existing_order,
    delete_existing_order
)

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderResponse)
def create_order_route(order_data: OrderCreate, db: Session = Depends(get_db)):
    return create_new_order(db, order_data)

@router.get("/", response_model=list[OrderResponse])
def get_all_orders_route(db: Session = Depends(get_db)):
    return get_orders(db)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order_by_id_route(order_id: int, db: Session = Depends(get_db)):
    order = get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=OrderResponse)
def update_order_route(order_id: int, order_data: OrderUpdate, db: Session = Depends(get_db)):
    order = update_existing_order(db, order_id, order_data)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/{order_id}")
def delete_order_route(order_id: int, db: Session = Depends(get_db)):
    success = delete_existing_order(db, order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}
