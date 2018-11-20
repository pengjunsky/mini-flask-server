from sqlalchemy import Column, Integer

from app.models.base import Base


class Order2Product(Base):
    __tablename__ = 'order_product'
    order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False)
    property_id = Column(Integer)
    count = Column(Integer, nullable=False)