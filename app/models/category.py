from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.libs.error_code import CategoryException
from app.models.base import Base, db
from app.models.image import Image


class Category(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    topic_img_id = Column(Integer, ForeignKey('image.id'))

    def keys(self):
        self.hide('topic_img_id').append('image')
        return self.fields

    @property
    def image(self):
        if self.topic_img_id:
            return Image.get_img_by_id(self.topic_img_id).url
        else:
            return None

    @staticmethod
    def get_all_categories():
        with db.auto_check_empty(CategoryException):
            return Category.query.all()
