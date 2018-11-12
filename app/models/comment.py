from sqlalchemy import Column, String, Integer

from app.libs.error_code import UserException, NotFound

from app.models.base import Base, db
from app.models.user import User


class Comment(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    content = Column(String(100))
    type = Column(Integer, default=1)  # 1好评 2中评 3差评

    def keys(self):
        self.hide('product_id', 'uid').append('userInfo')
        return self.fields

    @property
    def userInfo(self):
        with db.auto_check_empty(UserException):
            return User.query.filter_by(id=self.uid).first_or_404().hide('email', 'auth')

    @staticmethod
    def get_comment_by_pid(pid):
        with db.auto_check_empty(NotFound):
            return Comment.query.filter_by(product_id=pid).all()
