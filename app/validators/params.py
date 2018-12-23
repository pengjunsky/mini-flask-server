from sqlalchemy import and_
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, ValidationError, length
from app.libs.error_code import CartException
from app.models.base import db
from app.models.cart import Cart
from app.models.order import Order
from app.models.product import Product
from app.models.product_property import Product2Property
from app.models.user_address import UserAddress
from app.models.user_coupon import UserCoupon
from app.validators.base import BaseValidator


class Count(BaseValidator):
    count = IntegerField(default=20)
    page = IntegerField(default=0)
    type = IntegerField(default=0)

    def validate_count(self, value):
        if not self.isPositiveInteger(value.data) or not (1 <= int(value.data) <= 20):
            raise ValidationError(message='count必须是[1, 20]区间内 的正整数')

    def validate_page(self, value):
        if value.data:
            if not self.isPositiveInteger(value.data):
                raise ValidationError(message='page必须是正整数')

    def validate_type(self, value):
        if value.data:
            if not self.isPositiveInteger(value.data):
                raise ValidationError(message='type必须是正整数')


class IDMustBePositiveInt(Count):
    id = IntegerField(validators=[DataRequired()])

    def validate_id(self, value):
        if not self.isPositiveInteger(value.data):
            raise ValidationError(message='id must be positive integer')


class CartAddValidator(BaseValidator):
    product_id = IntegerField(validators=[DataRequired()])
    property_id = IntegerField()
    qty = IntegerField(default=1)

    def validate_product_id(self, value):
        if not self.isPositiveInteger(value.data):
            raise ValidationError(message='product_id must be positive integer')
        if not Product.query.filter_by(id=value.data).first():
            raise ValidationError(message='the resource are not found')

    def validate_property_id(self, value):
        if not value.data:
            return
        if not self.isPositiveInteger(value.data):
            raise ValidationError(message='property_id must be positive integer')
        if not Product2Property.query.filter_by(id=value.data).first():
            raise ValidationError(message='the resource are not found')

    def validate_qty(self, value):
        if not self.isPositiveInteger(value.data):
            raise ValidationError(message='qty must be positive integer')
        if self.property_id.data:
            property = Product2Property.query.filter_by(id=self.property_id.data).first()
            if property:
                if value.data > property.stock:
                    raise ValidationError(message='qty greater than stock')
        else:
            product = Product.query.filter_by(id=self.product_id.data).first()
            if product:
                if value.data > product.stock:
                    raise ValidationError(message='qty greater than stock')


class CartIdsValidator(BaseValidator):
    cart_ids = StringField(validators=[DataRequired()])

    def validate_cart_ids(self, value):
        cart_ids = value.data
        if not isinstance(cart_ids, list):
            raise ValidationError(message='购物车参数不正确')
        if len(cart_ids) == 0:
            raise ValidationError(message='购物车列表不能为空')
        for cart_id in cart_ids:
            if not self.isPositiveInteger(cart_id):
                raise ValidationError(message='购物车列表参数错误')
            else:
                with db.auto_check_empty(CartException()):
                    Cart.query.filter_by(id=cart_id).first_or_404()


class ProductIdValidator(BaseValidator):
    product_ids = StringField(validators=[DataRequired()])

    def validate_product_ids(self, value):
        if not isinstance(value.data, list):
            raise ValidationError(message='参数不正确')
        for ids in value.data:
            if len(ids) == 0:
                raise ValidationError(message='参数不能为空')
            if 'product_id' not in ids.keys():
                raise ValidationError(message='product_id参数不存在')
            else:
                if not self.isPositiveInteger(ids['product_id']):
                    raise ValidationError(message='product_id must be positive integer')
            if 'property_id' in ids.keys():
                if ids['property_id']:
                    if not self.isPositiveInteger(ids['property_id']):
                        raise ValidationError(message='property_id must be positive integer')
            if 'qty' not in ids.keys():
                raise ValidationError(message='qty参数不存在')
            else:
                if not self.isPositiveInteger(ids['qty']):
                    raise ValidationError(message='qty must be positive integer')


class OrderCouponValidator(BaseValidator):
    coupon_ids = StringField(validators=[DataRequired()])

    def validate_coupon_ids(self, value):
        if not isinstance(value.data, list):
            raise ValidationError(message='参数不正确')
        for ids in value.data:
            if 'product_id' not in ids.keys():
                raise ValidationError(message='product_id参数不存在')
            else:
                if not self.isPositiveInteger(ids['product_id']):
                    raise ValidationError(message='product_id must be positive integer')
            if 'category_id' not in ids.keys():
                raise ValidationError(message='category_id参数不存在')
            else:
                if not self.isPositiveInteger(ids['category_id']):
                    raise ValidationError(message='category_id must be positive integer')
            if 'total' not in ids.keys():
                raise ValidationError(message='total参数不存在')
            else:
                if not self.isPositivePrice(ids['total']):
                    raise ValidationError(message='total must be positive integer')


class CreateOrderValidator(ProductIdValidator):
    address_id = IntegerField(validators=[DataRequired()])
    user_coupon_id = IntegerField()
    remark = StringField(validators=[length(max=100, message='最多100个字')])

    def validate_address_id(self, value):
        if not self.isPositiveInteger(value.data):
            raise ValidationError(message='address_id must be positive integer')
        if not UserAddress.query.filter_by(id=value.data).first():
            raise ValidationError(message='the resource are not found')

    def validate_user_coupon_id(self, value):
        if not value.data:
            return
        if not self.isPositiveInteger(value.data):
            raise ValidationError(message='user_coupon_id must be positive integer')
        if not UserCoupon.query.filter_by(id=value.data).first():
            raise ValidationError(message='the resource are not found')


class CreateCommentValidator(BaseValidator):
    order_id = StringField(validators=[DataRequired()])
    comment = StringField(validators=[DataRequired()])
    length = None

    def validate_order_id(self, value):
        order = Order.query.filter(and_(Order.order_no == value.data, Order.status == 4)).first()
        if not order:
            raise ValidationError(message='the resource are not found')
        self.length = len(order.snap_product)

    def validate_comment(self, value):
        if not isinstance(value.data, list):
            raise ValidationError(message='参数不正确')
        if self.length:
            if not self.length == len(value.data):
                raise ValidationError(message='评价条数不正确')
        for i in value.data:
            if 'product_id' not in i.keys():
                raise ValidationError(message='product_id参数不存在')
            else:
                if not self.isPositiveInteger(i['product_id']):
                    raise ValidationError(message='product_id must be positive integer')
                if not Product.query.filter_by(id=i['product_id']).first():
                    raise ValidationError(message='the resource are not found')
            if not (len(i['content']) <= 100):
                raise ValidationError(message='content最大长度100')
            if not self.isPositiveInteger(i['type']) or not (1 <= int(i['type']) <= 3):
                raise ValidationError(message='type必须是[1, 3]区间内 的正整数')
