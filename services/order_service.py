# services/order_service.py

from sqlalchemy.orm import Session
from schemas.order import OrderCreate, OrderResponse, OrderItemResponse
from models.order import Order
from repositories.order_repository import (
    create_order_db,
    get_all_orders_db,
    get_order_by_id_db,
    update_order_db,
    delete_order_db
)

# -----------------------------
# Universal mapping function
# -----------------------------
def map_order_to_response(order: Order) -> OrderResponse:
    return OrderResponse(
        order_id=order.order_id,
        user_id=order.user_id,
        user_name=order.user_name,
        email=order.email,
        phone=order.phone,
        shipping_address=order.shipping_address,
        items=[
            OrderItemResponse(
                product_id=item.product_id,
                product_name=item.product_name,
                quantity=item.quantity,
                price_per_unit=item.price_per_unit
            )
            for item in order.items
        ],
        total_amount=order.total_amount,
        status=order.status.value,
        notes=order.notes,
        created_at=order.created_at,
        updated_at=order.updated_at
    )

# -----------------------------
# CRUD service functions
# -----------------------------
def create_order(db: Session, order_data: OrderCreate) -> OrderResponse:
    order = create_order_db(db, order_data)
    return map_order_to_response(order)

def get_all_orders(db: Session) -> list[OrderResponse]:
    orders = get_all_orders_db(db)
    return [map_order_to_response(o) for o in orders]

def get_order(db: Session, order_id: int) -> OrderResponse | None:
    order = get_order_by_id_db(db, order_id)
    if not order:
        return None
    return map_order_to_response(order)

def update_existing_order(db: Session, order_id: int, order_data: OrderCreate | None) -> OrderResponse | None:
    order = update_order_db(db, order_id, order_data)
    if not order:
        return None
    return map_order_to_response(order)

def delete_existing_order(db: Session, order_id: int) -> bool:
    return delete_order_db(db, order_id)
