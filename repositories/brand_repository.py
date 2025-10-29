from sqlalchemy.orm import Session
from models.brand import Brand, Product
from schemas.brand import BrandCreate

def create_brand_db(db: Session, brand_data: BrandCreate ) -> Brand:
    brand = Brand(
        brand_name = brand_data.brand_name,
        country = brand_data.country,
        website = brand_data.website, 
    )

    db.add(brand)

    db.flush()

    for product in brand_data.products:
        products = Product(
            product_id = product.product_id,
            brand_id = brand.brand_id,
            productType = product.productType,
            productName = product.productName,
            price = product.price

        )
        db.add(products)
    db.commit()
    db.refresh(brand)
    return brand


def get_all_products_db(db: Session):
    return db.query(Product).all()