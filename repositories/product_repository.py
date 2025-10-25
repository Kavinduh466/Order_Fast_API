# repositories/order_repository.py
from sqlalchemy.orm import Session
from models import product
from models.product import Product
from schemas.product import ProductCreate,ProductUpdate

def create_product_db(db: Session, product_data: ProductCreate) -> Product:
    product = Product(
        product_id = product_data.prodcutId,
        product_name = product_data.productName,
        description = product_data.description,
        sku = product_data.sku,
        quantity = product_data.quantity,
        price = product_data.price,
        category_id = product_data.category_id,
        created_at = product_data.created_at,
        updated_at = product_data.updated_at,
    )
    db.add(product)
    db.flush()  

    db.commit()
    db.refresh(product)
    return product

def get_all_product_db(db: Session):
    return db.query(Product).all()

def get_product_by_id_db(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.prodcutId == product_id).first()

def update_product_db(db: Session, product_id: int, data: ProductUpdate) -> Product | None:
    product = db.query(Product).filter(Product.prodcutId == product_id).first()
    if not product:
        return None
    if data.productName is not None:
        product.productName = data.productName
    db.commit()
    db.refresh(product)
    return product

def delete_product_db(db: Session, product_id: int) -> bool:
    product = db.query(Product).filter(Product.prodcutId == product_id).first()
    if not product:
        return False
    db.delete(product)
    db.commit()
    return True
