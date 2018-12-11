from app.libs.error import APIException


class Success(APIException):
    code = 200
    msg = 'success'
    error_code = 0


class RenewSuccess(APIException):
    code = 201
    error_code = 1
    msg = 'renew success'


class DeleteSuccess(Success):
    code = 202
    msg = 'delete success'
    error_code = 2


class ServerError(APIException):
    code = 500
    msg = 'sorry, we make a mistake!'
    error_code = 999


class WeChatException(ServerError):
    code = 500
    msg = '微信服务器接口调用失败'
    error_code = 998


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class DuplicateGift(APIException):
    code = 400
    msg = 'the current book has already in gift'
    error_code = 2001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class ForbiddenException(APIException):
    code = 403
    msg = 'forbidden, not in scope'
    error_code = 1004


class StockException(APIException):
    code = 403
    msg = 'larger than stock'
    error_code = 3001


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 1001


class UserException(NotFound):
    code = 404
    msg = '指定的用户不存在，请检查参数'
    error_code = 1002


class ProductException(NotFound):
    code = 404
    msg = '指定的商品不存在，请检查参数'
    error_code = 1003


class PropertyException(NotFound):
    code = 404
    msg = '指定的商品规格不存在，请检查参数'
    error_code = 1004


class BannerMissException(NotFound):
    code = 404
    msg = '请求的Banner不存在'
    error_code = 1005


class CategoryException(NotFound):
    code = 404
    msg = '指定的类目不存在, 请检查参数'
    error_code = 1006


class CartException(NotFound):
    code = 404
    msg = '购物车商品不存在, 请检查参数'
    error_code = 1007

