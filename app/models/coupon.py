from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy import Column, String, Integer
from app.models.base import Base
from datetime import datetime


class Coupon(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(FLOAT(precision=6, scale=2), nullable=False)
    title = Column(String(24), nullable=False)
    label = Column(String(50), nullable=False)
    qty = Column(Integer, default=0)
    n_price = Column(Integer)
    n_product = Column(Integer)
    n_category = Column(Integer)
    dead_time = Column(Integer, nullable=False)

    @staticmethod
    def get_all_coupon():
        current_time = int(int(datetime.now().timestamp()))
        return Coupon.query.filter(Coupon.dead_time > current_time).all()
