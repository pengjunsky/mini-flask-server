from flask import jsonify

from app.libs.redprint import RedPrint
from app.models.banner import Banner
from app.validators.params import IDMustBePositiveInt

api = RedPrint('banner')


@api.route('/<int:id>', methods=['GET'])
def get_banner(id):
    id = IDMustBePositiveInt().validate_for_api().id.data
    banner = Banner.get_banner_by_id(id=id)
    return jsonify(banner)