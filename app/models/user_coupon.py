from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, SmallInteger, and_
from sqlalchemy.orm import relationship
from app.models.base import Base


class UserCoupon(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    coupon_id = Column(Integer, ForeignKey('coupon.id'), nullable=False)
    status = Column(SmallInteger, default=1)
    coupon = relationship('Coupon')

    def keys(self):
        self.hide('user_id', 'coupon_id', 'status').append('coupon')
        return self.fields

    @staticmethod
    def get_user_coupon_all(uid):
        current_time = int(int(datetime.now().timestamp()))
        coupons = UserCoupon.query.filter(and_(UserCoupon.user_id == uid, UserCoupon.status == 1)).all()
        user_coupon = []
        for coupon in coupons:
            if coupon.coupon.dead_time > current_time:
                user_coupon.append(coupon)
        return user_coupon

    @staticmethod
    def get_order_coupon(coupon_ids, uid):
        user_coupon = UserCoupon.get_user_coupon_all(uid)
        coupons = []
        total_price = 0
        for ids in coupon_ids:
            total_price += ids['total']
            for i in user_coupon:
                if ids['product_id'] == i.coupon.n_product or ids['category_id'] == \
                        i.coupon.n_category or \
                        (total_price > i.coupon.n_price if i.coupon.n_price else None):
                    if i not in coupons:
                        coupons.append(i)
        return coupons
