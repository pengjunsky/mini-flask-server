from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.dialects.mysql import FLOAT

from app.models.base import Base


class Order(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_no = Column(String(20), unique=True, nullable=False)
    user_id = Column(Integer, unique=True, nullable=False)
    total_price = Column(FLOAT(precision=6, scale=2), nullable=False)
    snap_img = Column(String(255))
    snap_name = Column(String(80))
    total_count = Column(Integer, unique=True, nullable=False)
    snap_items = Column(Text)
    snap_address = Column(String(500))
    prepay_id = Column(String(100))
    status = Column(Boolean, default=1, nullable=False)
