from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import FLOAT
from app.models.base import Base


class OrderSnap(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_no = Column(String(20), unique=True, nullable=False)
    snap_name = Column(String(80), nullable=False)
    snap_img = Column(String(255), nullable=False)
    price = Column(FLOAT(precision=6, scale=2), nullable=False)
    property_name = Column(String(30))
    count = Column(Integer, nullable=False)

    def keys(self):
        self.hide('order_no')
        return self.fields
