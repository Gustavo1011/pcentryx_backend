from exceptions.new_exceptions.not_enabled_exist_exception import NotEnabledExistException
from functions.utils.util import get_model, snake_case
from managers.class_utils.validator.validator import Validator


class ValidatorEnabledExist(Validator):
    """Class for validator Exist"""

    def __init__(self, model, field_model, field_data):
        self.model = get_model(model)
        self.field_model = field_model
        self.field_data = field_data
        self.deleted = [getattr(self.model, 'deleted') == "False"]
        self.enabled = [getattr(self.model, 'is_enabled') == "True"]
        self.query = None

    def validate(self, data, vars_):
        if data.get(self.field_data) is not None:
            if self.not_enabled_exist(data):
                raise NotEnabledExistException(self.field_data)
            vars_[snake_case(self.model.__name__)] = self.query.first()

    def not_enabled_exist(self, data):
        """Verifica si existe ID"""
        self.query = self.model.query.filter(
            getattr(self.model, self.field_model) == data.get(self.field_data),
            *self.deleted,
            *self.enabled
        )
        return self.query.count() == 0
