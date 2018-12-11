from flask import g, jsonify

from app.libs.error_code import Success, UserException
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.order import Order
from app.models.order_snap import OrderSnap
from app.models.user import User
from app.service.wxpay import UnifiedOrder, OrderQuery
from app.validators.params import CreateOrderValidator

api = RedPrint('order')


@api.route('/<string:oid>', methods=['GET'])
def get_one_order(oid):
    order = Order.get_one_order(oid)
    return jsonify(order)


@api.route('/pay/<string:oid>', methods=['GET'])
@auth.login_required
def get_pay_order(oid):
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first().append('openid')
    order = Order.get_one_order(oid)
    wx_pay = UnifiedOrder(oid, user.openid, order.pay_price)
    pay_info = wx_pay.get_pay_info()
    return jsonify(pay_info)


@api.route('/pay/query/<string:oid>', methods=['GET', 'POST'])
def get_pay_query(oid):
    pay_info = OrderQuery(oid).get_pay_info()
    if pay_info['result_code'] == 'FAIL':
        return UserException(msg=pay_info['err_code'])
    elif pay_info['trade_state'] == 'SUCCESS':
        with db.auto_commit():
            order = Order.get_one_order(oid)
            order.transaction_id = pay_info['transaction_id']
            order.status = 2
        return Success(msg=pay_info['trade_state_desc'])
    return Success(msg=pay_info['trade_state_desc'])


@api.route('/pay/notify', methods=['POST'])
def get_pay_notify():
    pass


@api.route('/create', methods=['POST'])
@auth.login_required
def create_order():
    uid = g.user.uid
    form = CreateOrderValidator().validate_for_api()
    order_no = Order.create_order(form.product_ids.data, form.address_id.data,
                                  form.user_coupon_id.data, form.remark.data, uid)

    return jsonify(order_no)
