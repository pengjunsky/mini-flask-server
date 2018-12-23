from sqlalchemy import Column, String, Integer

from app.libs.error_code import UserException, NotFound

from app.models.base import Base, db
from app.models.order import Order
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
    def get_comment_by_pid(pid, count, page):
        with db.auto_check_empty(NotFound):
            return Comment.query.filter_by(product_id=pid).limit(count).offset(page).all()

    @staticmethod
    def create_by_comment(uid, order_id, comment):
        for i in comment:
            with db.auto_commit():
                comment = Comment()
                comment.uid = uid
                comment.type = i['type']
                comment.content = i['content']
                comment.product_id = i['product_id']
                db.session.add(comment)
        with db.auto_commit():
            order = Order.query.filter_by(order_no=order_id).first_or_404()
            order.status = 5
            order.update()
