from flask import jsonify, g

from app.libs.error_code import RenewSuccess, UserException
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from app.models.user_address import UserAddress
from app.validators.forms import AddressNew

api = RedPrint('address')


@api.route('', methods=['GET'])
@auth.login_required
def get_address():
    uid = g.user.uid
    # with db.auto_check_empty(UserException(error_code=6001, msg='用户地址不存在')):
    user_address = UserAddress.query.filter_by(user_id=uid).first()
    return jsonify(user_address)


@api.route('/renew', methods=['POST'])
@auth.login_required
def renew_address():
    uid = g.user.uid
    address_info = AddressNew().validate_for_api().data
    with db.auto_check_empty(UserException):
        user = User.query.filter_by(id=uid).first_or_404()
    user.save_address(address_info, uid)
    user_address = UserAddress.query.filter_by(user_id=uid).first()
    return jsonify(user_address)
