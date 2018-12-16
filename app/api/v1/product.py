from flask import jsonify
from app.libs.redprint import RedPrint
from app.models.product import Product
from app.validators.params import Count, IDMustBePositiveInt, ProductIdValidator

api = RedPrint('product')


@api.route('/recent', methods=['GET', 'POST'])
def get_recent():
    form = Count().validate_for_api()
    products = Product.get_most_recent(form.count.data, form.page.data)
    return jsonify(products)


@api.route('/by_category', methods=['GET', 'POST'])
def get_all_in_category():
    form = IDMustBePositiveInt().validate_for_api()
    products = Product.get_product_by_category_id(form.id.data, form.count.data, form.page.data)
    return jsonify(products)


@api.route('/<int:id>', methods=['GET', 'POST'])
def get_one(id):
    product = Product.get_product_detail(id=id)
    return jsonify(product)


@api.route('/order_product', methods=['POST'])
def get_order_product():
    form = ProductIdValidator().validate_for_api()
    o_product = []
    for ids in form.product_ids.data:
        o_product.append(Product.get_order_product(ids))
    return jsonify(o_product)
