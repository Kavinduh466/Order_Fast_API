from sqlalchemy.orm import Session
from schemas.brand import BrandCreate,BrandResponse
from models.brand import Brand
from repositories.brand_repository import (
    create_brand_db,
    get_all_products_db
)

def map_brand_to_response(brand :Brand) -> BrandResponse:
    return BrandResponse(
        brand_id = Brand.brand_id,
        brand_name = Brand.brand_name,
        country = Brand.country,
        products = Brand.products,
        website = Brand.website
    )


def create_brand(db: Session, brand_data: BrandCreate ) -> BrandResponse:
    brand = create_brand_db(db, brand_data)
    return map_brand_to_response(brand)

def get_all_brands(db: Session) -> list[BrandResponse]:
    brands = get_all_products_db(db)
    return [map_brand_to_response(b) for b in brands]

