from sqlalchemy.orm import Session
from models.brand import Brand, Product
from schemas.brand import BrandCreate, BrandUpdate

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
    return db.query(Brand).all()


def get_brand_by_id_db(db: Session, brand_id: int) -> Brand | None:
    return db.query(Brand).filter(Brand.brand_id == brand_id).first()

def update_brand_by_id_db(db: Session, brand_id: int, brand_data: BrandUpdate) -> Brand | None:
    brand = db.query(Brand).filter(Brand.brand_id == brand_id).first()
    if not brand:
        return None

    if brand_data.brand_name is not None:
        brand.brand_name = brand_data.brand_name
    if brand_data.country is not None:
        brand.country = brand_data.country
    if brand_data.website is not None:
        brand.website = brand_data.website

    if brand_data.products and len(brand_data.products) > 0:
        for product_data in brand_data.products:
            product = db.query(Product).filter(
                Product.product_id == product_data.product_id,
                Product.brand_id == brand_id
            ).first()

            if product:
                product.productType = product_data.productType
                product.productName = product_data.productName
                product.price = product_data.price
            else:
                new_product = Product(
                    product_id=product_data.product_id,
                    brand_id=brand.brand_id,
                    productType=product_data.productType,
                    productName=product_data.productName,
                    price=product_data.price
                )
                db.add(new_product)

    db.commit()
    db.refresh(brand)
    return brand

 
def delete_brand_by_id_db(db: Session, brand_id:int):
        brand = db.query(Brand).filter(Brand.brand_id == brand_id).first()
        if not brand:
            return False
        db.delete(brand)
        db.commit()
        return True

     
