from flask import g, jsonify

from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.cart import Cart

api = RedPrint('cart')


@api.route('', methods=['GET'])
@auth.login_required
def get_cart():
    uid = g.user.uid
    # uid = 1
    carts = Cart.get_cart_by_uid(uid)
    return jsonify(carts)