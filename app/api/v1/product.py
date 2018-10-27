from flask import jsonify

from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.product import Product
from app.validators.params import Count, IDMustBePositiveInt

api = RedPrint('product')


# @api.route('', methods=['GET'])
# def get_recent():
#     products = Product.query.filter_by().all()
#     return jsonify(products)
#     # return jsonify('11')


@api.route('/recent', methods=['GET'])
def get_recent():
    count = Count().validate_for_api().count.data
    products = Product.get_most_recent(count=count)
    return jsonify(products)
#
#
# @api.route('/by_category', methods=['GET'])
# def get_all_in_category():
#     id = IDMustBePositiveInt().validate_for_api().id.data
#     products = Product.get_product_by_category_id(id=id)
#     return jsonify(products)
#
#
# @api.route('/<int:id>', methods=['GET'])
# def get_one(id):
#     id = IDMustBePositiveInt().validate_for_api().id.data
#     product = Product.get_product_detail(id=id)
#     return jsonify(product)
#
#
# @api.route('/<int:id>', methods=['DELETE'])
# def delete_one(id):
#     id = IDMustBePositiveInt().validate_for_api().id.data
#     product = Product.get_product_detail(id=id)
#     return Success()
