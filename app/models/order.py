from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from app.models.base import Base


class Order(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_no = Column(String(20), unique=True, nullable=False)
    user_id = Column(Integer, unique=True, nullable=False)
    total_price = Column(FLOAT(precision=6, scale=2), nullable=False)
    snap_product_id = Column(Integer, ForeignKey('order_snap.id'), nullable=False)
    snap_product = relationship('OrderSnap')
    snap_address = Column(String(500), nullable=False)
    coupon_price = Column(FLOAT(precision=6, scale=2),)
    remark = Column(String(100))
    prepay_id = Column(String(100))
    status = Column(SmallInteger, default=1, nullable=False)  # '1:未支付， 2：已支付，3：已发货 , 4: 已支付，但库存不足'

    def keys(self):
        self.hide('user_id', 'snap_product_id')
        return self.fields
