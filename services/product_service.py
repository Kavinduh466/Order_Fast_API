from sqlalchemy.orm import Session
from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from models.product import Product
from repositories.product_repository import (
    create_product_db,
    get_all_product_db,
    get_product_by_id_db,
    update_product_db,
    delete_product_db
)

def map_product_to_response(product: Product) -> ProductResponse:
    return ProductResponse(
        productName=product.prodcutId,
        description=product.description,
        sku=product.sku,
        quantity=product.quantity,
        price=product.price,
        created_at=product.created_at,
        updated_at=product.updated_at
    
    )

def create_product(db: Session, product_data: ProductCreate) -> ProductResponse:
    product = create_product_db(db, product_data)
    return map_product_to_response(product)

def get_all_products(db: Session) -> list[ProductResponse]:
    products = get_all_product_db(db)
    return [map_product_to_response(p) for p in products]

def get_product(db: Session, product_id: int) -> ProductResponse | None:
    product = get_product_by_id_db(db, product_id)
    if not product:
        return None
    return map_product_to_response(product)

def update_existing_product(db: Session, product_id: int, product_data: ProductUpdate | None) -> ProductResponse | None:
    product = update_product_db(db, product_id, product_data)
    if not product:
        return None
    return map_product_to_response(product)

def delete_existing_product(db: Session, product_id: int) -> bool:
    return delete_product_db(db, product_id)