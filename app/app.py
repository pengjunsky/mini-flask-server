from datetime import date

from flask.json import JSONEncoder as _JSONEncoder
from flask import Flask as _Flask, _request_ctx_stack

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
