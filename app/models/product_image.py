from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger

from app.models.base import Base
from app.models.image import Image


class Product2Image(Base):
    __tablename__ = 'product_image'
    id = Column(Integer, primary_key=True, autoincrement=True)
    img_id = Column(Integer, ForeignKey('image.id'), nullable=False)
    order = Column(Integer, nullable=False, default=0)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    type = Column(SmallInteger, default=0)

    def keys(self):
        self.hide('id', 'img_id', 'product_id', 'order', 'type').append('img_url')
        return self.fields

    @property
    def img_url(self):
        return Image.get_img_by_id(id=self.img_id).url