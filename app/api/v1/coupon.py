from flask import jsonify, g
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.coupon import Coupon
from app.models.user_coupon import UserCoupon
from app.validators.params import OrderCouponValidator, Count

api = RedPrint('coupon')


@api.route('/all', methods=['GET', 'POST'])
def get_coupon():
    form = Count().validate_for_api()
    coupon = Coupon.get_all_coupon(form.count.data, form.page.data)
    return jsonify(coupon)


@api.route('/my', methods=['GET', 'POST'])
@auth.login_required
def get_user_coupon():
    uid = g.user.uid
    form = Count().validate_for_api()
    coupon = UserCoupon.get_user_coupon_all(uid, form.count.data, form.page.data)
    return jsonify(coupon)


@api.route('/order', methods=['POST'])
@auth.login_required
def get_order_coupon():
    uid = g.user.uid
    form = OrderCouponValidator().validate_for_api()
    order_coupon = UserCoupon.get_order_coupon(form.coupon_ids.data, uid)
    return jsonify(order_coupon)
