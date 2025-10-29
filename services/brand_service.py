from sqlalchemy.orm import Session
from schemas.brand import BrandCreate, BrandResponse, ProductItemResponse, BrandUpdate
from models.brand import Brand
from repositories.brand_repository import (
    create_brand_db,
    get_all_products_db,
    get_brand_by_id_db,
    update_brand_by_id_db,
    delete_brand_by_id_db
)

def map_brand_to_response(brand: Brand) -> BrandResponse:
    return BrandResponse(
        brand_id=brand.brand_id,
        brand_name=brand.brand_name,
        country=brand.country,
        website=brand.website,
        products=[
            ProductItemResponse(
                product_id=product.product_id,
                product_name=product.productName,  
                product_type=product.productType,  
                price=product.price
            )
            for product in brand.products
        ]
    )


def create_brand(db: Session, brand_data: BrandCreate) -> BrandResponse:
    brand = create_brand_db(db, brand_data)
    return map_brand_to_response(brand)


def get_all_brands(db: Session) -> list[BrandResponse]:
    brands = get_all_products_db(db)
    return [map_brand_to_response(b) for b in brands]

def get_brand_by_id_service(db: Session, brand_id: int) -> BrandResponse:
    brand = get_brand_by_id_db(db, brand_id)
    return map_brand_to_response(brand)

def update_brand_by_id_service(db: Session, brand_id: int, brand_data: BrandUpdate) -> BrandResponse:
    brand = update_brand_by_id_db(db, brand_id,brand_data)
    return map_brand_to_response(brand)

def delete_brand_by_id_service(db: Session, brand_id: int):
    return delete_brand_by_id_db(db, brand_id)