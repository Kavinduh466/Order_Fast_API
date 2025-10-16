# repositories/order_repository.py
from sqlalchemy.orm import Session
from models.order import Order, OrderItem
from schemas.order import OrderCreate, OrderUpdate

def create_order_db(db: Session, order_data: OrderCreate) -> Order:
    order = Order(
        user_id=order_data.user_id,
        shipping_address=order_data.shipping_address,
        total_amount=0
    )
    db.add(order)
    db.flush()  # get order_id

    total = 0
    for item in order_data.items:
        order_item = OrderItem(
            order_id=order.order_id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_per_unit=10.0  # dummy price
        )
        total += order_item.quantity * order_item.price_per_unit
        db.add(order_item)

    order.total_amount = total
    db.commit()
    db.refresh(order)
    return order

def get_all_orders_db(db: Session):
    return db.query(Order).all()

def get_order_by_id_db(db: Session, order_id: int) -> Order | None:
    return db.query(Order).filter(Order.order_id == order_id).first()

def update_order_db(db: Session, order_id: int, data: OrderUpdate) -> Order | None:
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if not order:
        return None
    if data.shipping_address is not None:
        order.shipping_address = data.shipping_address
    if data.status is not None:
        order.status = data.status
    if data.notes is not None:
        order.notes = data.notes
    db.commit()
    db.refresh(order)
    return order

def delete_order_db(db: Session, order_id: int) -> bool:
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if not order:
        return False
    db.delete(order)
    db.commit()
    return True

