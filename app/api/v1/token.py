from datetime import datetime

from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import TokenValidator, ClientValidator
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

api = RedPrint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientValidator().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify_by_email,
        ClientTypeEnum.USER_MINA: User.verify_by_wx
    }
    identity = promise[ClientTypeEnum(form.type.data)](form.account.data, form.secret.data)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration)
    return jsonify(token), 201


@api.route('/secret', methods=['POST'])
def get_token_info():
    """获取令牌信息"""
    form = TokenValidator().validate_for_api()
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(form.token.data, return_header=True)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)

    r = {
        'scope': data[0]['scope'],
        'create_at': datetime.fromtimestamp(data[1]['iat']),  # 创建时间
        'expire_in': datetime.fromtimestamp(data[1]['exp']),  # 有效期
        'uid': data[0]['uid']
    }
    return jsonify(r)


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    token = s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
    return {'token': token.decode('ascii')}
