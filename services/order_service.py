from sqlalchemy.orm import Session
from schemas.order import OrderCreate, OrderUpdate
from repositories.order_repository import (
    create_order,
    get_all_orders,
    get_order_by_id,
    update_order,
    delete_order
)

def create_new_order(db: Session, order_data: OrderCreate):
    return create_order(db, order_data)

def get_orders(db: Session):
    orders = get_all_orders(db)
    if not orders:
        # return empty list instead of raising error
        return []
    return orders

def get_order(db: Session, order_id: int):
    order = get_order_by_id(db, order_id)
    if not order:
        # return a dict message instead of None, router can check this
        return {"message": "Order not found"}
    return order

def update_existing_order(db: Session, order_id: int, order_data: OrderUpdate):
    order = update_order(db, order_id, order_data)
    if not order:
        return {"message": "Order not found"}
    return order

def delete_existing_order(db: Session, order_id: int):
    success = delete_order(db, order_id)
    if not success:
        return {"message": "Order not found"}
    return {"message": "Order deleted successfully"}
