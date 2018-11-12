from wtforms import IntegerField
from wtforms.validators import DataRequired, ValidationError

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
    num = IntegerField(default='1')

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

    def validate_num(self, value):
        if not self.isPositiveInteger(value.data):
            raise ValidationError(message='num must be positive integer')
        if self.property_id.data:
            property = Product2Property.query.filter_by(id=self.property_id.data).first()
            if value.data > property.stock:
                raise ValidationError(message='num greater than stock')
        else:
            product = Product.query.filter_by(id=self.product_id.data).first()
            print(value.data)
            print(product.stock)
            if value.data > product.stock:
                raise ValidationError(message='num greater than stock')
