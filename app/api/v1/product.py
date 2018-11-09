from flask import jsonify
from app.libs.redprint import RedPrint
from app.models.product import Product
from app.validators.params import Count, IDMustBePositiveInt

api = RedPrint('product')


@api.route('/recent', methods=['GET', 'POST'])
def get_recent():
    count = Count().validate_for_api().count.data
    products = Product.get_most_recent(count=count)
    return jsonify(products)


@api.route('/by_category', methods=['GET', 'POST'])
def get_all_in_category():
    id = IDMustBePositiveInt().validate_for_api().id.data
    products = Product.get_product_by_category_id(id=id)
    return jsonify(products)


@api.route('/<int:id>', methods=['GET', 'POST'])
def get_one(id):
    product = Product.get_product_detail(id=id)
    return jsonify(product)

