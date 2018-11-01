from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger

from app.models.base import Base

class Product2Property(Base):
    __tablename__ = 'product_property'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    detail = Column(String(255), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)