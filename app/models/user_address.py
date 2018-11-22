from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import Base


class UserAddress(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    mobile = Column(String(20), nullable=False)
    province = Column(String(20))
    city = Column(String(20))
    country = Column(String(20))
    detail = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)