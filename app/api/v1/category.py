from flask import jsonify

from app.libs.redprint import RedPrint
from app.models.category import Category

api = RedPrint('category')


@api.route('/all', methods=['GET'])
def get_all_category():
    category = Category.get_all_categories()
    return jsonify(category)
