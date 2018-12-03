from flask import jsonify, g
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.coupon import Coupon
from app.models.user_coupon import UserCoupon
from app.validators.params import OrderCouponValidator

api = RedPrint('coupon')


@api.route('/all', methods=['GET', 'POST'])
def get_coupon():
    coupon = Coupon.get_all_coupon()
    return jsonify(coupon)


@api.route('', methods=['GET', 'POST'])
@auth.login_required
def get_user_coupon():
    uid = g.user.uid
    coupon = UserCoupon.get_user_coupon_all(uid)
    return jsonify(coupon)


@api.route('/order', methods=['POST'])
@auth.login_required
def get_order_coupon():
    uid = g.user.uid
    form = OrderCouponValidator().validate_for_api()
    order_coupon = UserCoupon.get_order_coupon(form.coupon_ids.data, uid)
    return jsonify(order_coupon)
