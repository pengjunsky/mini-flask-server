from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, ValidationError
from app.validators.base import BaseValidator


class IDMustBePositiveInt(BaseValidator):
    id = IntegerField(validators=[DataRequired()])

    def validate_id(self, value):
        id = value.data
        if not self.isPositiveInteger(id):
            raise ValidationError(message='id must be positive integer')
        self.id.data = id


class Count(BaseValidator):
    count = IntegerField(default='15')

    def validate_count(self, value):
        count = value.data
        if not self.isPositiveInteger(count) or not (1 <= int(count) <= 15):
            raise ValidationError(message='count必须是[1, 15]区间内 的正整数')
        self.count.data = int(count)
