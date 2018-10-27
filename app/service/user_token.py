from flask import current_app

from app.libs.error_code import WeChatException
from app.libs.httper import Http


class UserToken:
    def __init__(self, code):
        self.code = code
        self.wx_app_id = current_app.config['APP_ID']
        self.wx_app_secret = current_app.config['APP_SECRET']
        self.wx_login_url = current_app.config['LOGIN_URL'].format(self.wx_app_id, self.wx_app_secret, self.code)

    def get(self):
        wx_result = Http.get(self.wx_login_url)
        if not wx_result:
            raise Exception()
        else:
            if 'errcode' in wx_result.keys():
                self.__process_login_error(wx_result)
            else:
                return wx_result

    def __process_login_error(self, wx_result):
        raise WeChatException(
            msg=wx_result['errmsg'],
            error_code=wx_result['errcode'],
        )