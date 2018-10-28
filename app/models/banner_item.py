from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.image import Image


class BannerItem(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    banner_id = Column(Integer, ForeignKey('banner.id'), nullable=False)
    image = relationship('Image')
    img_id = Column(Integer, ForeignKey('image.id'), nullable=False)
    key_word = Column(String(100), nullable=False)
    type = Column(SmallInteger, default=1)

    def keys(self):
        self.hide('banner_id', 'img_id').append('img_url')
        return self.fields

    @property
    def img_url(self):
        return Image.get_img_by_id(id=self.img_id).url
