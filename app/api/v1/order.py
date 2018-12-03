from flask import g

from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.validators.params import CreateOrderValidator

api = RedPrint('order')


@api.route('/create', methods=['POST'])
@auth.login_required
def create_order():
    uid = g.user.uid
    form = CreateOrderValidator().validate_for_api()
    return '1'