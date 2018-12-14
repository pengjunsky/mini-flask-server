from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201


class ScopeEnum(Enum):
    User = 1
    Admin = 2
    Super = 3


class StatusEnum(Enum):
    CLOSED = 0
    NOT_PAY = 1
    SUC_PAY = 2
    DELIVERY = 3
    NOT_EST = 4
    FINISH = 5
