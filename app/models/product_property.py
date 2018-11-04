from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT

from app.models.base import Base


class Product2Property(Base):
    __tablename__ = 'product_property'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    price = Column(FLOAT(precision=6, scale=2), nullable=False)
    stock = Column(Integer, default=0)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)

    def keys(self):
        self.hide('product_id')
        return self.fields
