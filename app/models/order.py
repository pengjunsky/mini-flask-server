from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship
from datetime import datetime
from time import time
from random import randint
from app.models.base import Base, db
from app.models.order_snap import OrderSnap
from app.models.product import Product


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_no = Column(String(20), unique=True, nullable=False)
    user_id = Column(Integer, unique=True, nullable=False)
    total_price = Column(FLOAT(precision=6, scale=2), nullable=False)
    snap_address = Column(String(500), nullable=False)
    coupon_price = Column(FLOAT(precision=6, scale=2), )
    remark = Column(String(100))
    prepay_id = Column(String(100))
    status = Column(SmallInteger, default=1, nullable=False)  # '1:未支付， 2：已支付，3：已发货 , 4: 已支付，但库存不足'

    def keys(self):
        self.hide('user_id', 'snap_product_id').append('snap_product')
        return self.fields

    @property
    def snap_product(self):
        try:
            snap_product = OrderSnap.query.filter_by(order_no=self.order_no).all()
        except Exception:
            return None
        return snap_product

    @staticmethod
    def create_order(product_ids, address_id, user_coupon_id, remark):
        order_no = Order.make_order_no()
        o_products = []
        for ids in product_ids:
            o_products.append(Product.get_order_product(ids))
        OrderSnap.add_order_snap(o_products, order_no)

    @staticmethod
    def make_order_no():
        now = datetime.now()
        timestamp = time()
        y_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        order_sn = y_code[now.year - 2018] + hex(now.month).upper() + str(now.day) \
                   + str('%.6f' % timestamp)[-6:] + str(timestamp)[2: 7] \
                   + str(randint(0, 99))
        return order_sn
