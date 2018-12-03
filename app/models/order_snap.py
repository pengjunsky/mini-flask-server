from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT
from app.models.base import Base
from app.models.image import Image


class OrderSnap(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_no = Column(String(20), unique=True, nullable=False)
    snap_name = Column(String(80), nullable=False)
    snap_img_id = Column(Integer, ForeignKey('image.id'), nullable=False)
    price = Column(FLOAT(precision=6, scale=2), nullable=False)
    property_name = Column(String(30))
    count = Column(Integer, nullable=False)

    def keys(self):
        self.hide('order_no').append('snap_img')
        return self.fields

    @property
    def snap_img(self):
        return Image.get_img_by_id(self.main_img_id).url
