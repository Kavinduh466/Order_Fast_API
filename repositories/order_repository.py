from sqlalchemy.orm import Session
from models.order import Order, OrderItem, OrderStatusEnum
from schemas.order import OrderCreate, OrderUpdate
from datetime import datetime, timezone

def create_order(db: Session, order_data: OrderCreate):
    total_amount = 0.0

    order = Order(
        user_id=order_data.user_id,
        shipping_address=order_data.shipping_address,
        total_amount=0.0,
        created_at=datetime.now(timezone.utc),
    )
    db.add(order)
    db.flush()

    for item in order_data.items:
        price_per_unit = 100.0  # fake product price
        total_amount += item.quantity * price_per_unit
        order_item = OrderItem(
            order_id=order.order_id,
            product_id=item.product_id,
            product_name=f"Product {item.product_id}",
            quantity=item.quantity,
            price_per_unit=price_per_unit,
        )
        db.add(order_item)

    order.total_amount = total_amount
    db.commit()
    db.refresh(order)
    return order

def get_all_orders(db: Session):
    return db.query(Order).all()

def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.order_id == order_id).first()

def update_order(db: Session, order_id: int, order_data: OrderUpdate):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if not order:
        return None

    if order_data.shipping_address:
        order.shipping_address = order_data.shipping_address
    if order_data.status:
        order.status = OrderStatusEnum(order_data.status)
    if order_data.notes:
        order.notes = order_data.notes
    order.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(order)
    return order

def delete_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if not order:
        return False
    db.delete(order)
    db.commit()
    return True
