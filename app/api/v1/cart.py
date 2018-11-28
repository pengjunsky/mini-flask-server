from flask import g, jsonify

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.cart import Cart
from app.validators.params import CartAddValidator, CartIdsValidator

api = RedPrint('cart')


@api.route('', methods=['GET', 'POST'])
@auth.login_required
def get_cart():
    uid = g.user.uid
    carts = Cart.get_cart_by_uid(uid)
    return jsonify(carts)


@api.route('/add', methods=['GET', 'POST'])
@auth.login_required
def add_cart():
    uid = g.user.uid
    form = CartAddValidator().validate_for_api()
    Cart.add_cart(uid, form.product_id.data, form.property_id.data, form.qty.data)
    return Success()


@api.route('/del', methods=['POST'])
@auth.login_required
def del_cart():
    uid = g.user.uid
    form = CartIdsValidator().validate_for_api()
    Cart.del_cart(uid, form.cartIds.data)
    return DeleteSuccess()
