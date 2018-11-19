from sqlalchemy import Column, Integer, ForeignKey, and_

from app.libs.error_code import NotFound, ProductException, PropertyException
from app.models.base import Base, db
from app.models.product import Product
from app.models.product_property import Product2Property


class Cart(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    property_id = Column(Integer, ForeignKey('product_property.id'))
    uid = Column(Integer, nullable=False)
    num = Column(Integer, default=1)

    def keys(self):
        self.hide('product_id', 'property_id', 'uid').append('product', 'property')
        return self.fields

    @property
    def product(self):
        with db.auto_check_empty(ProductException):
            return Product.query.filter_by(id=self.product_id).first_or_404().hide('summary', 'sale', 'stock')

    @property
    def property(self):
        if self.property_id:
            with db.auto_check_empty(PropertyException):
                return Product2Property.query.filter_by(id=self.property_id).first_or_404().hide('stock')

    @staticmethod
    def get_cart_by_uid(uid):
        with db.auto_check_empty(NotFound):
            return Cart.query.filter_by(uid=uid).all()

    @staticmethod
    def add_cart(uid, product_id, property_id, num):
        old_cart = Cart.query.filter(and_
                                     (Cart.uid == uid, Cart.product_id == product_id,
                                      Cart.property_id == property_id)).first()
        if not old_cart:
            with db.auto_commit():
                cart = Cart()
                cart.product_id = product_id
                cart.property_id = property_id
                cart.num = num
                cart.uid = uid
                db.session.add(cart)
        else:
            with db.auto_commit():
                old_cart.num += num
                old_cart.update()

    @staticmethod
    def del_cart(uid, cids):
        for cid in cids:
            with db.auto_commit():
                cart = Cart.query.filter(and_(Cart.uid == uid, Cart.id == cid)).first()
                db.session.delete(cart)
