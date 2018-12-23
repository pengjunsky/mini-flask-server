from sqlalchemy import Column, Integer, String, SmallInteger, and_, desc
from sqlalchemy.dialects.mysql import FLOAT
from datetime import datetime
from time import time
from random import randint
from app.libs.error_code import UserException
from app.models.base import Base, db
from app.models.order_snap import OrderSnap
from app.models.product import Product
from app.models.product_property import Product2Property
from app.models.user_address import UserAddress
from app.models.user_coupon import UserCoupon


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_no = Column(String(20), unique=True, nullable=False)
    mail_no = Column(String(20))
    user_id = Column(Integer, nullable=False)
    total_price = Column(FLOAT(precision=6, scale=2), nullable=False)
    pay_price = Column(FLOAT(precision=6, scale=2), nullable=False)
    snap_address = Column(String(500), nullable=False)
    coupon_price = Column(FLOAT(precision=6, scale=2), default=0)
    postage = Column(Integer, default=0)
    remark = Column(String(100))
    transaction_id = Column(String(100))
    status = Column(SmallInteger, default=1, nullable=False)  # 0: 已关闭 '1:未支付， 2：已支付，3：已发货, 4: 待评价, 5: 已完成

    def keys(self):
        self.append('snap_product', 'create_time')
        return self.fields

    @property
    def snap_product(self):
        try:
            snap_product = OrderSnap.query.filter_by(order_no=self.order_no).all()
        except Exception:
            return None
        return snap_product

    @staticmethod
    def create_order(product_ids, address_id, user_coupon_id, remark, uid):
        order_no = Order.__make_order_no()
        o_products = []
        for ids in product_ids:
            o_products.append(Product.get_order_product(ids))
        with db.auto_check_empty(UserException(error_code=6001, msg='地址不存在')):
            user_address = UserAddress.query.filter_by(id=address_id).first()
            snap_address = user_address.name + ' ' + user_address.mobile + ' ' + user_address.detail
        if user_coupon_id:
            with db.auto_check_empty(UserException(error_code=7001, msg='优惠卷不存在')):
                coupon_price = UserCoupon.query.filter(and_(UserCoupon.id == user_coupon_id,
                                                            UserCoupon.status == 1)).first().coupon.price
        else:
            coupon_price = 0
        total_price = Order.__product_to_calculate(o_products)[0]
        postage = Order.__product_to_calculate(o_products)[1]
        with db.auto_commit():
            order = Order()
            order.order_no = order_no
            order.user_id = uid
            order.snap_address = snap_address
            order.coupon_price = coupon_price
            order.remark = remark
            order.total_price = total_price
            order.postage = postage
            order.pay_price = total_price + postage - coupon_price
            OrderSnap.add_order_snap(o_products, order_no)
            Order.__minus_product_stock(o_products)
            Order.__revise_user_coupon(user_coupon_id)
            db.session.add(order)
        return order_no

    # 生成唯一订单号
    @staticmethod
    def __make_order_no():
        now = datetime.now()
        timestamp = time()
        y_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        order_sn = y_code[now.year - 2018] + hex(now.month).upper() + str(now.day) \
                   + str('%.6f' % timestamp)[-6:] + str(timestamp)[2: 7] \
                   + str(randint(100, 999))
        return order_sn

    @staticmethod
    def __product_to_calculate(o_products):
        total_price = 0
        multiple = 100
        nums = []
        for i in o_products:
            nums.append(i['postage'])
            if i['property']:
                total_price += (i['qty'] * (i['property']['price'] * multiple)) / multiple
            else:
                total_price += (i['qty'] * (i['price'] * multiple)) / multiple
        postage = min(nums)
        return total_price, postage

    @staticmethod
    def __minus_product_stock(o_products):
        for i in o_products:
            with db.auto_commit():
                if i['property']:
                    product_property = Product2Property.query.filter_by(id=i['property']['id']).first_or_404()
                    product_property.stock -= i['qty']
                    db.session.add(product_property)
                else:
                    product = Product.query.filter_by(id=i['id']).first_or_404()
                    product.stock -= i['qty']

    @staticmethod
    def restore_product_stock(o_products):
        for i in o_products:
            with db.auto_commit():
                if i['property_id']:
                    product_property = Product2Property.query.filter_by(id=i['property_id']).first_or_404()
                    product_property.stock += i['count']
                    db.session.add(product_property)
                else:
                    product = Product.query.filter_by(id=i['product_id']).first_or_404()
                    product.stock += i['count']

    @staticmethod
    def __revise_user_coupon(user_coupon_id):
        if user_coupon_id:
            with db.auto_commit():
                user_coupon = UserCoupon.query.filter(and_(UserCoupon.id == user_coupon_id,
                                                           UserCoupon.status == 1)).first()
                user_coupon.status = 0

    @staticmethod
    def get_one_order(oid):
        with db.auto_commit():
            return Order.query.filter_by(order_no=oid).first_or_404()

    @staticmethod
    def get_user_order(uid, count, page, type):
        if not type:
            with db.auto_commit():
                return Order.query.filter_by(user_id=uid).order_by(desc(Order.create_time)).limit(count).offset(page).all()
        else:
            with db.auto_commit():
                return Order.query.filter(Order.user_id == uid, Order.status == type).order_by(desc(Order.create_time)).limit(count).offset(page).all()

    @staticmethod
    def get_user_order_count(uid):
        with db.auto_commit():
            orders = Order.query.filter_by(user_id=uid).all()
        status = {'NOT_PAY': 0, 'SUC_PAY': 0, 'DELIVERY': 0, 'NOT_EST': 0}
        if orders:
            for order in orders:
                if order.status == 1:
                    status['NOT_PAY'] += 1
                elif order.status == 2:
                    status['SUC_PAY'] += 1
                elif order.status == 3:
                    status['DELIVERY'] += 1
                elif order.status == 4:
                    status['NOT_EST'] += 1
        return status
