from flask import g
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.order import Order
from app.models.order_snap import OrderSnap
from app.validators.params import CreateOrderValidator

api = RedPrint('order')


@api.route('/create', methods=['POST'])
@auth.login_required
def create_order():
    uid = g.user.uid
    form = CreateOrderValidator().validate_for_api()
    order = Order.create_order(form.product_ids.data, form.address_id.data,
                               form.user_coupon_id.data, form.remark.data)
    return '1'