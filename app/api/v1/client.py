from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import RedPrint

from app.models.user import User
from app.validators.forms import ClientValidator, UserEmailValidator

api = RedPrint('client')


@api.route('/register', methods=['GET', 'POST'])
def create_client():
    form = ClientValidator().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailValidator().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)


