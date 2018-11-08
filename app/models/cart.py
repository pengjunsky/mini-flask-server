from sqlalchemy import Column, Integer, ForeignKey, orm
from sqlalchemy.orm import relationship

from app.libs.error_code import NotFound, ProductException
from app.models.base import Base, db
from app.models.product import Product
from app.models.product_property import Product2Property


class Cart(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    property_id = Column(Integer, ForeignKey('product_property.id'), nullable=False)
    uid = Column(Integer, nullable=False)
    number = Column(Integer, default=1)

    def keys(self):
        self.hide('product_id', 'property_id', 'uid').append('product', 'property')
        return self.fields

    @property
    def product(self):
        with db.auto_check_empty(ProductException):
            return Product.query.filter_by(id=self.product_id).first_or_404().hide('summary', 'sale', 'stock')

    @property
    def property(self):
        with db.auto_check_empty(ProductException):
            return Product2Property.query.filter_by(id=self.property_id).first_or_404().hide('stock')

    @staticmethod
    def get_cart_by_uid(uid):
        with db.auto_check_empty(NotFound):
            return Cart.query.filter_by(uid=uid).all()
            # carts = Cart.query.filter_by(uid=uid).all()
            # print(carts)
            # if carts:
            #     # carts = [cart.hide('product') for cart in carts]
            #     return carts
            # else:
            #     return []
