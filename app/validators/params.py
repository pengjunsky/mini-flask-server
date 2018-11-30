from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, ValidationError

from app.libs.error_code import CartException
from app.models.base import db
from app.models.cart import Cart
from app.models.product import Product
from app.models.product_property import Product2Property
from app.validators.base import BaseValidator


class IDMustBePositiveInt(BaseValidator):
    id = IntegerField(validators=[DataRequired()])

    def validate_id(self, value):
        if not self.isPositiveInteger(value.data):
            raise ValidationError(message='id must be positive integer')


class Count(BaseValidator):
    count = IntegerField(default='20')

    def validate_count(self, value):
        if not self.isPositiveInteger(value.data) or not (1 <= int(value.data) <= 20):
            raise ValidationError(message='count必须是[1, 20]区间内 的正整数')


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
    cartIds = StringField(validators=[DataRequired()])

    def validate_cartIds(self, value):
        cartIds = value.data
        if not isinstance(cartIds, list):
            raise ValidationError(message='购物车参数不正确')
        if len(cartIds) == 0:
            raise ValidationError(message='购物车列表不能为空')
        for cartId in cartIds:
            if not self.isPositiveInteger(cartId):
                raise ValidationError(message='购物车列表参数错误')
            else:
                with db.auto_check_empty(CartException()):
                    Cart.query.filter_by(id=cartId).first_or_404()


class ProductIdValidator(BaseValidator):
    ids = StringField(validators=[DataRequired()])

    def validate_ids(self, value):
        if not isinstance(value.data, list):
            raise ValidationError(message='参数不正确')
        for ids in value.data:
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
    data = StringField(validators=[DataRequired()])

    def validate_data(self, value):
        if not isinstance(value.data, list):
            raise ValidationError(message='参数不正确')
        for data in value.data:
            if 'product_id' not in data.keys():
                raise ValidationError(message='product_id参数不存在')
            else:
                if not self.isPositiveInteger(data['product_id']):
                    raise ValidationError(message='product_id must be positive integer')
            if 'category_id' not in data.keys():
                raise ValidationError(message='category_id参数不存在')
            else:
                if not self.isPositiveInteger(data['category_id']):
                    raise ValidationError(message='category_id must be positive integer')
            if 'total' not in data.keys():
                raise ValidationError(message='total参数不存在')
            else:
                if not self.isPositivePrice(data['total']):
                    raise ValidationError(message='total must be positive integer')