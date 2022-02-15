from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.not_exist_exception import NotExistException
from functions.utils.util import get_model, snake_case


class ValidatorExist(Validator):
    """Class for validator Exist"""
    def __init__(self, model, field_model, field_data):
        self.model = get_model(model)
        self.field_model = field_model
        self.field_data = field_data
        self.deleted = [getattr(self.model, 'deleted') == "False"]
        self.query = None

    def validate(self, data, vars_):
        if self.not_exist(data):
            raise NotExistException(self.field_data)
        vars_[snake_case(self.model.__name__)] = self.query.first()

    def not_exist(self, data):
        """Verifica si existe ID"""
        self.query = self.model.query.filter(
            getattr(self.model, self.field_model) == data[self.field_data],
            *self.deleted
        )
        return self.query.count() == 0
