from app.libs.error_code import DeleteSuccess, RenewSuccess
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from flask import jsonify, g

from app.validators.forms import UserInfoValidator

api = RedPrint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        db.session.delete(user)
    return DeleteSuccess()


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        db.session.delete(user)
    return DeleteSuccess()


@api.route('/renew', methods=['POST'])
@auth.login_required
def update_user():
    uid = g.user.uid
    form = UserInfoValidator().validate_for_api()
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.nickname = form.nickname.data
        user.userPic = form.userPic.data
        user.update()
    return RenewSuccess()
