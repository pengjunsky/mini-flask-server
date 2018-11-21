from sqlalchemy import Column, Integer

from app.libs.error_code import ProductException, PropertyException
from app.models.base import Base, db
from app.models.product import Product
from app.models.product_property import Product2Property


class Order2Product(Base):
    __tablename__ = 'order_product'
    order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False)
    property_id = Column(Integer)
    count = Column(Integer, nullable=False)

    def keys(self):
        self.hide('order_id', 'product_id', 'property_id').append('product', 'property')
        return self.fields

    @property
    def product(self):
        with db.auto_check_empty(ProductException):
            return Product.query.filter_by(id=self.product_id).first_or_404().hide('summary', 'sale')

    @property
    def property(self):
        if self.property_id:
            with db.auto_check_empty(PropertyException):
                return Product2Property.query.filter_by(id=self.property_id).first_or_404()