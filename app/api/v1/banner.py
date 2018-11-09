from flask import jsonify

from app.libs.redprint import RedPrint
from app.models.banner import Banner

api = RedPrint('banner')


@api.route('/<int:id>', methods=['GET', 'POST'])
def get_banner(id):
    banner = Banner.get_banner_by_id(id=id)
    return jsonify(banner)