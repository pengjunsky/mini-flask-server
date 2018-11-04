from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey, and_
from sqlalchemy import desc, asc
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from app.libs.error_code import ProductException
from app.models.image import Image

from app.models.product_image import Product2Image
from app.models.base import Base, db
from app.models.product_property import Product2Property


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    price = Column(FLOAT(precision=6, scale=2), nullable=False)
    stock = Column(Integer, default=0)
    sale = Column(Integer, default=0)
    category_id = Column(Integer, nullable=False)
    summary = Column(String(50))
    main_img_id = Column(Integer, ForeignKey('image.id'), nullable=False)

    # main_img = relationship('Image', foreign_keys=[main_img_id])

    def keys(self):
        self.hide('main_img_id').append('main_img')
        return self.fields

    @property
    def main_img(self):
        return Image.get_img_by_id(self.main_img_id).url

    @property
    def detail_img(self):
        try:
            detail_img = Product2Image.query.filter(
                and_(Product2Image.product_id == self.id, Product2Image.type == 1)) \
                .order_by(asc(Product2Image.order)).all()
        except Exception:
            return []
        return list(map(lambda x: x['img_url'], list(detail_img)))

    @property
    def banner_img(self):
        try:
            banner_img = Product2Image.query.filter(
                and_(Product2Image.product_id == self.id, Product2Image.type == 0)) \
                .order_by(asc(Product2Image.order)).all()
        except Exception:
            return []
        return list(map(lambda x: x['img_url'], list(banner_img)))

    @property
    def property(self):
        try:
            property = Product2Property.query.filter_by(product_id=self.id).all()
        except Exception:
            return []
        return property

    @staticmethod
    def get_most_recent(count):
        with db.auto_check_empty(ProductException):
            products = Product.query.order_by(desc(Product.create_time)).limit(count).all()
            products = [product.hide('category_id', 'stock', 'summary') for product in products]
            return products

    @staticmethod
    def get_product_by_category_id(id):
        with db.auto_check_empty(ProductException):
            products = Product.query.filter_by(category_id=id).all()
            products = [product.hide('category_id', 'stock', 'summary') for product in products]
            return products

    @staticmethod
    def get_product_detail(id):
        with db.auto_check_empty(ProductException):
            return Product.query.filter_by(id=id).first_or_404()\
                .hide('category_id').append('detail_img', 'banner_img', 'property')
