from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy import desc, asc
from sqlalchemy.dialects.mysql import FLOAT
from app.libs.error_code import ProductException

from app.models.m2m import Product2Image
from app.models.base import Base, db


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    price = Column(FLOAT(precision=6, scale=2), nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    category_id = Column(Integer, nullable=False)
    _main_img_url = Column('main_img_url', String(255))
    _from = Column('from', SmallInteger, default=1)
    summary = Column(String(50))
    img_id = Column(Integer)

    def keys(self):
        self.hide('_main_img_url', '_from', 'img_id').append('main_img_url')
        return self.fields

    @property
    def main_img_url(self):
        return self.get_url(self._main_img_url)

    @property
    def img_urls(self):
        try:
            img_urls = Product2Image.query.filter_by(product_id=self.id).order_by(asc(Product2Image.order)).all()
        except Exception:
            return []
        return list(map(lambda x: x['img_url'], list(img_urls)))

    @staticmethod
    def get_most_recent(count):
        with db.auto_check_empty(ProductException):
            return Product.query.order_by(desc(Product.create_time)).limit(count).all()

    @staticmethod
    def get_product_by_category_id(id):
        with db.auto_check_empty(ProductException):
            return Product.query.filter_by(category_id=id).all()

    @staticmethod
    def get_product_detail(id):
        with db.auto_check_empty(ProductException):
            return Product.query.filter_by(id=id).first_or_404().hide('category_id').append('img_urls')
